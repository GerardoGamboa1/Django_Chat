from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('<str:canal>/', views.canal, name='canal'),
    path('checkview', views.checkview, name="checkview"),
    path('enviar', views.enviar, name="enviar"),
    path('getMensajes/<str:canal>/', views.getMensajes, name='getMensajes'),
]
