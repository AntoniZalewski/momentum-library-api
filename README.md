# 📖 API & Panel Zarządzania Biblioteką

Projekt zrealizowany w ramach zadania rekrutacyjnego dla **The Momentum AI**. Jest to w pełni funkcjonalna, skonteneryzowana aplikacja Django do zarządzania księgozbiorem, składająca się z **API REST** oraz **zaawansowanego panelu administracyjnego** dla personelu biblioteki.

![Zrzut ekranu panelu admina](https://github.com/user-attachments/assets/7454d62e-8cd5-46b6-99b5-c9f36ae7a838)

---

## ✨ Kluczowe Funkcjonalności

Oprócz spełnienia podstawowych wymagań zadania, projekt został rozbudowany o szereg profesjonalnych funkcji, aby zapewnić jak najlepsze doświadczenie użytkownika (UX) i pokazać znajomość dobrych praktyk:

* **API REST** z pełną obsługą operacji CRUD dla zasobu książek.
* **W pełni skonteneryzowane środowisko** z Docker i Docker Compose dla łatwego i powtarzalnego uruchamiania.
* **Profesjonalny Panel Admina** z nowoczesnym motywem (`django-jazzmin`), zapewniający intuicyjny interfejs dla bibliotekarza.
* **Zaawansowane UX w Panelu:**
    * Wyszukiwanie i filtrowanie listy książek.
    * **Wizualne statusy** (dostępna/wypożyczona) dla lepszej czytelności.
    * **Akcje masowe** do jednoczesnego oznaczania wielu książek jako wypożyczone/zwrócone.
    * Przyciski akcji (Edytuj/Usuń) w każdym wierszu dla szybszej pracy.
* **Eksport danych** do formatów CSV, XLS, i innych, prosto z panelu admina.
* **Walidacja danych** na poziomie modelu, zapewniająca ich integralność (np. format numeru seryjnego).
* **Bezpieczna konfiguracja** z wykorzystaniem zmiennych środowiskowych (`.env`).

---

## 🚀 Uruchomienie

### Wymagania
* Zainstalowany [Git](https://git-scm.com/)
* Zainstalowany [Docker Desktop](https://www.docker.com/products/docker-desktop/)

### Kroki do Uruchomienia

1.  **Sklonuj repozytorium:**
    ```bash
    git clone [https://github.com/AntoniZalewski/momentum-library-api.git](https://github.com/AntoniZalewski/momentum-library-api.git)
    cd momentum-library-api
    ```

2.  **Stwórz plik konfiguracyjny `.env`:**
    *W głównym folderze projektu stwórz plik `.env` i wklej do niego poniższą zawartość:*
    ```env
    # Konfiguracja Bazy Danych
    POSTGRES_DB=momentum_db
    POSTGRES_USER=momentum_user
    POSTGRES_PASSWORD=momentum_password

    # Konfiguracja Django
    DJANGO_SECRET_KEY=super-secret-key-for-development
    DEBUG=True
    ```

3.  **Zbuduj i uruchom kontenery:**
    *Ta komenda postawi całe środowisko - aplikację webową oraz bazę danych.*
    ```bash
    docker compose up --build
    ```

4.  **Stwórz konto superużytkownika:**
    *Otwórz **drugi terminal** i wykonaj poniższą komendę, aby stworzyć konto administratora:*
    ```bash
    docker compose run --rm web python manage.py createsuperuser
    ```
    *Postępuj zgodnie z instrukcjami, aby ustawić nazwę, email i hasło.*

5.  **Zaloguj się i zaimportuj dane (Opcjonalnie):**
    * Wejdź do panelu admina pod adresem **http://localhost:8000/admin/** i zaloguj się.
    * Przejdź do sekcji **Książki**.
    * Kliknij zielony przycisk **`IMPORT`** w prawym górnym rogu.
    * Wybierz z dysku plik `books_to_import.csv`, który znajduje się w folderze projektu.
    * Przejdź przez kroki importu, a baza danych zostanie zapełniona przykładowymi książkami.

6.  **Gotowe!**
    * Panel administracyjny jest dostępny pod adresem: 👉 **http://localhost:8000/admin/**
    * API jest dostępne pod adresem: 👉 **http://localhost:8000/api/**

---

## 🛠️ Stos Technologiczny

* **Backend:** Python, Django, Django REST Framework
* **Baza Danych:** PostgreSQL
* **Konteneryzacja:** Docker
* **Panel Admina:** Django Admin, `django-jazzmin`, `django-import-export`