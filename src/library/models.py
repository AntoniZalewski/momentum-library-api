from django.db import models
from django.core.validators import RegexValidator

# Wspólny walidator dla wszystkich 6-cyfrowych numerów w systemie.
six_digit_validator = RegexValidator(r'^\d{6}$', 'Numer musi składać się z dokładnie 6 cyfr.')

# Główny model w naszej aplikacji - reprezentuje pojedynczą książkę.
class Book(models.Model):
    serial_number = models.CharField(
        max_length=6,
        unique=True,
        validators=[six_digit_validator],
        verbose_name="Numer seryjny",
        help_text="Unikalny, 6-cyfrowy numer seryjny książki."
    )
    title = models.CharField(max_length=200, verbose_name="Tytuł")
    author = models.CharField(max_length=100, verbose_name="Autor")
    
    # Pola związane ze statusem wypożyczenia
    is_borrowed = models.BooleanField(default=False, verbose_name="Wypożyczona")
    borrowed_date = models.DateField(null=True, blank=True, verbose_name="Data wypożyczenia")
    borrower_id = models.CharField(
        max_length=6,
        validators=[six_digit_validator],
        null=True,
        blank=True,
        verbose_name="ID wypożyczającego",
        help_text="6-cyfrowy numer z karty bibliotecznej czytelnika."
    )

    class Meta:
        verbose_name = "Książka"
        verbose_name_plural = "Książki"
        ordering = ['title', 'author'] # Domyślne sortowanie na listach

    def __str__(self):
        # Ustawiam "ludzką" reprezentację obiektu, przydatną np. w panelu admina.
        return f'"{self.title}" - {self.author} ({self.serial_number})'