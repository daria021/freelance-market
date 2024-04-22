from django.urls import path

from . import views

urlpatterns = [
    path(r'executor/<int:executor_id>/', views.executor_profile, name='executor'),
    path(r'client/<int:client_id>/', views.client_profile, name='client')
]
