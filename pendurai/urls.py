"""
URL configuration for pendurai project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from cadastro import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('cadastro/', views.cadastro_clientes, name='cadastro_clientes'),
    path('conta/', views.conta, name='conta'),
    path('adicionar_conta/<int:cliente_id>/', views.adicionar_conta, name='adicionar_conta'),
    path('buscar_clientes/', views.buscar_clientes, name='buscar_clientes'),
    path('form_cadastro_cliente/', views.form_cadastro_cliente, name='form_cadastro_cliente'),
    path('remover_cliente/<int:cliente_id>/', views.remover_cliente, name='remover_cliente'),
    path('listar_fiados/<int:cliente_id>/', views.lista_fiados_cliente, name='lista_fiados_cliente'),
    path('pagamento_parcial/<int:cliente_id>/', views.pagamento_parcial, name='pagamento_parcial'),
    path('atualizar_lista_clientes/', views.atualizar_lista_clientes, name='atualizar_lista_clientes'),
]
