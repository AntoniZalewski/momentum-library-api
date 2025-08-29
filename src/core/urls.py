from django.contrib import admin
from django.urls import path, include # Upewnij się, że jest tu 'include'

urlpatterns = [
    path('admin/', admin.site.urls),

    # Mój nowy wpis. Wszystkie zapytania na '/api/'
    # będą przekazywane do pliku urls.py z aplikacji 'library'.
    path('api/', include('library.urls')),
]