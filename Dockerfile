# Jako bazę wybieram oficjalny, odchudzony obraz Pythona.
FROM python:3.11-slim-buster

# Ustawiam zmienne środowiskowe, żeby zoptymalizować działanie Pythona w kontenerze.
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Ustawiam główny katalog roboczy wewnątrz kontenera.
WORKDIR /app

# Kopiuję najpierw sam plik z zależnościami, żeby wykorzystać cache Dockera.
COPY requirements.txt .

# Instaluję wszystko, co jest w requirements.txt.
RUN pip install --no-cache-dir -r requirements.txt

# Na końcu kopiuję wszystko z bieżącego folderu do kontenera.
COPY . .

# Ustawiam katalog roboczy na folder z kodem Django.
WORKDIR /app/src