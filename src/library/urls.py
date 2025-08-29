from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

# Tworzę instancję routera. DefaultRouter automatycznie stworzy też
# stronę główną API, którą zaraz zobaczymy.
router = DefaultRouter()

# Rejestruję mój BookViewSet w routerze.
# 'books' - to będzie prefiks URL dla endpointów książek (np. /api/books/).
# BookViewSet - widok, który ma być podłączony.
# basename - nazwa dla generowanych URLi.
router.register(r'books', BookViewSet, basename='book')

# Standardowa zmienna, której szuka Django.
# Dołączam automatycznie wygenerowane przez router adresy URL.
urlpatterns = [
    path('', include(router.urls)),
]