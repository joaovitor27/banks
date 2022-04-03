
from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('listagem/', views.listagem, name='listagem'),
    path('consulta/', views.consulta, name='consulta'),
]
