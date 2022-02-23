from django.urls import path
from .import views

urlpatterns = [
    path('user', views.home),
    path('registrarUser/', views.registrarUser),
    path('edicionUser/<codigo>', views.edicionUser),
    path('editarUser/', views.editarUser),
    path('eliminarUser/<codigo>', views.eliminarUser),
]

