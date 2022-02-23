from django.urls import path
from .import views

urlpatterns = [
    path('report', views.home2),
    path('registrarReport/', views.registrarReport),
    path('edicionReport/<codigo>', views.edicionReport),
    path('editarReport/', views.editarReport),
    path('eliminarReport/<codigo>', views.eliminarReport)
]