from django.http.response import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from cadastro.forms import CadastroForm, ContaForm
from cadastro.models import Cadastro, Conta
from django.db.models import Q, Sum


# Create your views here.
def index(request):
    clientes = Cadastro.objects.all()
    clientes_com_debitos = []

    for cliente in clientes:
        total_debitos = Conta.objects.filter(cliente=cliente).aggregate(Sum('valor'))['valor__sum'] or 0.0
        clientes_com_debitos.append({
            'cliente': cliente,
            'total_debitos': total_debitos
        })

    context = {'clientes_com_debitos': clientes_com_debitos}
    return render(request, 'index.html', context)

def lista_fiados_cliente(request, cliente_id):
    cliente = get_object_or_404(Cadastro, id=cliente_id)
    fiado = Conta.objects.filter(cliente=cliente)
    total = fiado.aggregate(Sum('valor'))['valor__sum'] or 0.0  # Garante que `None` vire `0.0`
    form = ContaForm()
    return render(request, 'partials/lista_debitos_cliente.html', {'fiado': fiado, 'cliente': cliente, 'total': total, 'form': form})


def form_cadastro_cliente(request):
    if request.method == "POST":
        form = CadastroForm(request.POST)
        if form.is_valid():
            cliente = form.save()
            cliente.save()
            # Recalcular os débitos totais para cada cliente após adicionar um novo cliente
            clientes = Cadastro.objects.all()
            clientes_com_debitos = [
                {
                    'cliente': c,
                    'total_debitos': Conta.objects.filter(cliente=c).aggregate(Sum('valor'))['valor__sum'] or 0.0
                } for c in clientes
            ]
            # Renderizar a lista de clientes atualizada
            return render(request, 'partials/clientes_list.html', {'clientes_com_debitos': clientes_com_debitos})
    else:
        form = CadastroForm()

    return render(request, 'partials/form_cadastro_cliente.html', {'form': form})


def buscar_clientes(request):
    query = request.GET.get('q', '').strip()
    clientes = Cadastro.objects.filter(
        Q(nome__icontains=query) |
        Q(telefone__icontains=query)
    ) if query else Cadastro.objects.all()

    clientes_com_debitos = [
        {
            'cliente': cliente,
            'total_debitos': Conta.objects.filter(cliente=cliente).aggregate(Sum('valor'))['valor__sum'] or 0.0
        } for cliente in clientes
    ]

    return render(request, 'partials/clientes_list.html', {'clientes_com_debitos': clientes_com_debitos})


def adicionar_conta(request, cliente_id):
    cliente = get_object_or_404(Cadastro, id=cliente_id)

    if request.method == "POST":
        form = ContaForm(request.POST)
        if form.is_valid():
            # Salvar a nova conta
            fiado = form.save(commit=False)
            fiado.cliente = cliente
            fiado.save()

            # Atualizar a lista de débitos no modal
            fiado_list = Conta.objects.filter(cliente=cliente)
            total = fiado_list.aggregate(Sum('valor'))['valor__sum'] or 0.0
            context_modal = {
                'cliente': cliente,
                'fiado': fiado_list,
                'total': total,
                'form': ContaForm(),
            }

            return render(request, 'partials/lista_debitos_cliente.html', context_modal)

    # Caso não seja POST, retornar o formulário novamente
    form = ContaForm()
    return render(request, 'partials/form_adicionar_conta.html', {'form': form, 'cliente': cliente})


def remover_cliente(request, cliente_id):
    cliente = get_object_or_404(Cadastro, id=cliente_id)
    cliente.delete()
    # Renderiza novamente a lista de clientes sem o cliente removido
    clientes = Cadastro.objects.all()
    clientes_com_debitos = [
        {
            'cliente': c,
            'total_debitos': Conta.objects.filter(cliente=c).aggregate(Sum('valor'))['valor__sum'] or 0.0
        } for c in clientes
    ]

    return render(request, 'partials/clientes_list.html', {'clientes_com_debitos': clientes_com_debitos})

def cadastro_clientes(request):
    if request.method == "POST":
        form = CadastroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = CadastroForm()

    return render(request, 'cadastro_cliente.html', {'form': form})


def conta(request, cliente_id):
    clientes = get_object_or_404(Cadastro, id=cliente_id)
    if request.method == "POST":
        form = ContaForm(request.POST)
        conta_f = form.save()
        conta_f.save()
        return redirect('dashboard')
    else:
        form = ContaForm()
    return render(request, 'conta.html', {'form': form, 'clientes': clientes})


def pagamento_parcial(request, cliente_id):
    cliente = get_object_or_404(Cadastro, id=cliente_id)

    if request.method == "POST":
        valor = request.POST.get("valor")
        try:
            valor = float(valor)
            if valor > 0:
                valor = -valor  # Converte para negativo no backend

            # Registrar o pagamento como uma nova entrada na tabela
            Conta.objects.create(cliente=cliente, compra="Pagamento Parcial", valor=valor)

            # Atualizar a lista de débitos no modal
            fiado = Conta.objects.filter(cliente=cliente)
            total = fiado.aggregate(Sum('valor'))['valor__sum'] or 0.0
            context = {
                'cliente': cliente,
                'fiado': fiado,
                'total': total,
                'form': ContaForm(),
            }
            return render(request, 'partials/lista_debitos_cliente.html', context)

        except ValueError:
            return JsonResponse({'error': 'Valor inválido'}, status=400)
    return JsonResponse({'error': 'Método não permitido'}, status=405)


def atualizar_lista_clientes(request):
    clientes = Cadastro.objects.all()
    clientes_com_debitos = [
        {
            'cliente': cliente,
            'total_debitos': Conta.objects.filter(cliente=cliente).aggregate(Sum('valor'))['valor__sum'] or 0.0,
        } for cliente in clientes
    ]
    return render(request, 'partials/clientes_list.html', {'clientes_com_debitos': clientes_com_debitos})