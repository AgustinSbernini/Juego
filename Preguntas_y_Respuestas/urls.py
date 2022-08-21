from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('databases/', include('Base_de_Datos.urls')),
    path('',include('Juego.urls')),
]
