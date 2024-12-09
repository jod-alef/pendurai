# Penduraí

Penduraí é um sistema web desenvolvido para gerenciar clientes e débitos em um ambiente simples e eficiente. Ele permite:
- Cadastro de clientes.
- Gerenciamento de débitos (inclusão de compras, pagamentos parciais).
- Listagem de débitos detalhados de cada cliente.
- Atualizações dinâmicas com HTMX.

## Tecnologias Utilizadas
- **Backend**: Django 5.1.4
- **Frontend**: HTMX, Tailwind CSS, Flowbite
- **Banco de Dados**: SQL (configurável no Django)
- **Servidor**: Uvicorn (opcional para uso com FastAPI)
- **Outros**: Django Compressor para otimização de arquivos estáticos.

## Requisitos do Sistema
Certifique-se de ter as seguintes dependências instaladas:
- Python 3.10 ou superior
- Pipenv ou Virtualenv (opcional, para gerenciar ambientes virtuais)
- Banco de dados configurado (SQLite por padrão)

## Instalação das Dependências
As dependências estão listadas no arquivo `requirements.txt`. Instale-as com o comando:

```bash
pip install -r requirements.txt
```

# Configuração do Projeto
## 1. Configuração Inicial

Após instalar as dependências, configure o banco de dados e execute as migrações:
```bash
python manage.py makemigrations
python manage.py migrate
```
## 2. Arquivos Estáticos

Certifique-se de que o Tailwind CSS e os outros arquivos estáticos estão processados e disponíveis:
```bash
python manage.py compress
python manage.py collectstatic
```
## 3. Executando o Servidor

Inicie o servidor de desenvolvimento do Django com:
```bash
python manage.py runserver
```
Acesse o sistema em: http://127.0.0.1:8000/.

## 4. Execute o watcher do tailwindcss caso vá fazer alterações no frontend

```bash
npx tailwindcss ./static/src/input.css -o ./static/src/output.css --watch
```

# Funcionalidades
## 1. Gerenciamento de Clientes

    Cadastrar Cliente: Insira nome, CPF, e-mail, telefone e endereço de forma simples.
    Busca Dinâmica: Filtre clientes por nome ou telefone.

## 2. Débitos

    Adicionar Débitos: Insira compras associadas a um cliente específico.
    Pagamento Parcial: Registre pagamentos parciais com valores convertidos automaticamente para negativos.
    Listagem Detalhada: Visualize débitos e o total pendurado no modal dinâmico.

## 3. Atualizações Dinâmicas

    Integração com HTMX para evitar recarregamentos desnecessários da página.
    Respostas dinâmicas para inclusão de contas e atualizações na interface.

## 4. Rotas Disponíveis

### As rotas principais do sistema são:
    Rota                        Descrição
    /                           Página inicial com lista de clientes.
    /cadastro/	                Cadastro de novos clientes.
    /adicionar_conta/<id>/	    Adicionar débito a um cliente.
    /pagamento_parcial/<id>/	Registrar pagamento parcial de um cliente.
    /remover_cliente/<id>/	    Remover cliente da base de dados.
    /listar_fiados/<id>/	    Exibe lista de débitos do cliente no modal.

# Estrutura do Projeto
## Diretório cadastro/

### Contém os componentes principais do sistema:

    models.py: Define as classes Cadastro e Conta usadas para representar clientes e débitos.
    forms.py: Contém os formulários CadastroForm e ContaForm com widgets estilizados.
    views.py: Gerencia as principais operações, como listar clientes, adicionar débitos e registrar pagamentos.

### Templates

    Templates organizados no diretório templates/:
        index.html: Página inicial.
        partials/: Includes reutilizáveis, como a lista de débitos no modal.
        static/: CSS e outros arquivos estáticos

# Dependências Principais

### Veja algumas bibliotecas usadas no projeto:

    Django: Framework web principal.
    HTMX: Para atualizações dinâmicas no frontend.
    Tailwind CSS: Framework CSS para estilização.
    Tailwind Flowbite: Open-source tailwind components library  
    Django Compressor: Otimização de arquivos estáticos.

Para uma lista completa, consulte o arquivo requirements.txt.
### Contribuindo

## Sinta-se à vontade para abrir issues ou enviar pull requests.