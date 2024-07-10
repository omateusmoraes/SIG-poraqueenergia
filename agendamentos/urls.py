from django.urls import path
from . import views

urlpatterns = [

    path('agendamentos/', views.agendamento_list, name='agendamento_list'),
    path('agendamentos/add/', views.add_agendamento, name='add_agendamento'),
    path('agendamentos/edit/<int:agendamento_id>/', views.edit_agendamento, name='edit_agendamento'),
    path('agendamentos/delete/<int:agendamento_id>/', views.delete_agendamento, name='delete_agendamento'),
]