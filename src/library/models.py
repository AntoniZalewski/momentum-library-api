from django.db import models
from django.core.validators import RegexValidator

# Stworzyłem walidator, żeby pilnować formatu numerów.
# Użyję go zarówno dla numeru seryjnego książki, jak i karty czytelnika.
six_digit_validator = RegexValidator(r'^\d{6}$', 'Numer musi składać się z dokładnie 6 cyfr.')

class Book(models.Model):
    """
    Model reprezentujący książkę w bibliotece.
    """
    serial_number = models.CharField(
        max_length=6,
        unique=True,
        validators=[six_digit_validator],
        verbose_name="Numer seryjny"
    )
    title = models.CharField(max_length=200, verbose_name="Tytuł")
    author = models.CharField(max_length=100, verbose_name="Autor")
    is_borrowed = models.BooleanField(default=False, verbose_name="Wypożyczona")
    borrowed_date = models.DateField(null=True, blank=True, verbose_name="Data wypożyczenia")
    borrower_id = models.CharField(
        max_length=6,
        validators=[six_digit_validator],
        null=True,
        blank=True,
        verbose_name="ID wypożyczającego"
    )

    class Meta:
        verbose_name = "Książka"
        verbose_name_plural = "Książki"
        ordering = ['title', 'author'] # Domyślne sortowanie

    def __str__(self):
        # Ta metoda definiuje, jak obiekt będzie wyglądał jako tekst, np. w panelu admina.
        return f'"{self.title}" - {self.author} ({self.serial_number})'