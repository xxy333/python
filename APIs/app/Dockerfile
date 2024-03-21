# Základní obraz Debian s Pythonem
FROM python:3.9-slim

# Nastavení pracovního adresáře v kontejneru
WORKDIR /app

# Kopírování zdrojových souborů Python kódu do kontejneru
COPY . .

# Instalace závislostí pomocí pip (pokud jsou potřeba)
RUN pip install -r requirements.txt

# Instalace dodatečných nástrojů pomocí apt-get
RUN apt-get update && apt-get install -y iputils-ping net-tools && apt-get install telnet

# Příkaz pro spuštění vašeho Python skriptu
CMD ["python", "app.py"]
