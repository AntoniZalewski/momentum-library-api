from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    """
    Mój serializer dla modelu Book.
    Będzie odpowiedzialny za tłumaczenie obiektów Book na format JSON i odwrotnie.
    """
    class Meta:
        model = Book # Wskazuję, który model ma być serializowany.

        # 'fields = "__all__"' to prosta droga, by uwzględnić wszystkie pola z modelu.
        # W bardziej złożonych API mógłbym tu wymienić konkretne pola, np. ['id', 'title', 'author'].
        fields = "__all__"