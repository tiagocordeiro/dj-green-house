from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('liga/<int:pin>/', views.liga, name='liga'),
    path('desliga/<int:pin>/', views.desliga, name='desliga'),
]
