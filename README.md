# API & Panel Zarządzania Biblioteką

Aplikacja do zarządzania księgozbiorem, stworzona jako zadanie rekrutacyjne dla The Momentum AI. Projekt składa się z backendowego API REST oraz w pełni funkcjonalnego panelu administracyjnego do zarządzania danymi.

![Panel Administracyjny](https://github.com/user-attachments/assets/7454d62e-8cd5-46b6-99b5-c9f36ae7a838)

---

## Główne Funkcje

* **API REST:** Pełna obsługa operacji CRUD dla zasobu książek.
* **Panel Administracyjny:** Rozbudowany interfejs dla personelu, oparty o `django-jazzmin` z następującymi usprawnieniami:
    * Wyszukiwanie, filtrowanie i sortowanie danych.
    * Wizualne wskaźniki statusu wypożyczenia.
    * Akcje masowe (grupowe oznaczanie statusu).
    * Przyciski akcji (edycja/usuwanie) w każdym wierszu.
    * Dynamiczne blokowanie pól formularza w zależności od stanu obiektu.
* **Import/Eksport Danych:** Możliwość eksportu danych do formatów CSV/XLS i importu z plików.
* **Walidacja Danych:** Reguły walidacyjne na poziomie modelu zapewniające spójność danych (np. 6-cyfrowy format numerów).
* **Konteneryzacja:** Całość środowiska (aplikacja + baza danych) zarządzana przez Docker Compose.
* **Bezpieczna Konfiguracja:** Wykorzystanie zmiennych środowiskowych do zarządzania kluczami i danymi dostępowymi.

---

## Stos Technologiczny

* **Backend:** Python, Django, Django REST Framework
* **Baza Danych:** PostgreSQL
* **Konteneryzacja:** Docker
* **Narzędzia Dodatkowe:** `django-jazzmin`, `django-import-export`

---

## Instalacja i Uruchomienie

### Wymagania Wstępne

* Zainstalowany [Git](https://git-scm.com/)
* Zainstalowany [Docker Desktop](https://www.docker.com/products/docker-desktop/)

### Kroki Instalacji

1.  **Klonowanie Repozytorium:**
    Otwórz terminal i sklonuj repozytorium za pomocą poniższej komendy, a następnie przejdź do nowo utworzonego folderu.

    ```bash
    git clone https://github.com/AntoniZalewski/momentum-library-api.git
    cd momentum-library-api
    ```

2.  **Konfiguracja Środowiska:**
    W głównym folderze projektu stwórz plik `.env` na podstawie poniższego szablonu. Zawiera on dane konfiguracyjne, które nie są śledzone przez Git.

    ```env
    # Konfiguracja Bazy Danych
    POSTGRES_DB=momentum_db
    POSTGRES_USER=momentum_user
    POSTGRES_PASSWORD=momentum_password

    # Konfiguracja Django
    DJANGO_SECRET_KEY=super-secret-key-for-development
    DEBUG=True
    ```

3.  **Budowa i Uruchomienie Kontenerów:**
    To polecenie postawi całe środowisko - aplikację webową oraz bazę danych. Pierwsze uruchomienie może potrwać kilka minut.

    ```bash
    docker compose up --build
    ```
    *Serwer będzie działał w tym terminalu, zostaw go włączonego.*

4.  **Przygotowanie Bazy Danych:**
    Otwórz **drugi, nowy terminal**, wejdź do folderu z projektem i wykonaj poniższą komendę, aby stworzyć tabele w bazie danych.

    ```bash
    docker compose run --rm web python manage.py migrate
    ```

5.  **Tworzenie Konta Administratora:**
    W tym samym drugim terminalu stwórz konto potrzebne do zalogowania się w panelu.

    ```bash
    docker compose run --rm web python manage.py createsuperuser
    ```
    Postępuj zgodnie z instrukcjami, aby ustawić nazwę użytkownika, email i hasło.

6.  **Import Przykładowych Danych (Opcjonalnie):**
    Po zalogowaniu do panelu admina, przejdź do sekcji "Książki". Możesz użyć przycisku `IMPORT`, aby wgrać dane z dołączonego do repozytorium pliku `books_to_import.csv` i od razu zobaczyć aplikację w działaniu.

---

## Dostęp do Aplikacji

* **Panel Administracyjny:** [http://localhost:8000/admin/](http://localhost:8000/admin/)
* **Główny punkt API:** [http://localhost:8000/api/](http://localhost:8000/api/)