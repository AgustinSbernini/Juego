from django.urls import path
from . import views

urlpatterns = [
    path('forms/create/', views.create, name='create'),
    path('success/', views.success, name='success'),
    path('forms/updel/', views.updel, name='updel'),
    path('delete/', views.delete, name='delete'),
    path('update/', views.update, name='update'),
    path('updateSuccess/', views.updateSuccess, name='updateSuccess'),
]