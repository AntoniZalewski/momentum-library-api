from rest_framework.viewsets import ModelViewSet
from .models import Book
from .serializers import BookSerializer

class BookViewSet(ModelViewSet):
    """
    Mój ViewSet do zarządzania książkami.
    Dzięki ModelViewSet, DRF automatycznie zapewni mi pełen zestaw operacji
    CRUD (Create, Read, Update, Delete) bez pisania dodatkowej logiki.
    """
    # queryset to zbiór obiektów, na których ten ViewSet będzie operował.
    # W tym przypadku - wszystkie książki.
    queryset = Book.objects.all()

    # serializer_class wskazuje "tłumacza", którego ViewSet ma używać.
    serializer_class = BookSerializer