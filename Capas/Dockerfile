# Capa 1: la imagen base
FROM ubuntu:latest

# Capa nueva: actualiza la lista de paquetes e instala curl
RUN apt-get update && \
    apt-get install -y curl && \
    rm -rf /var/lib/apt/lists/*

# Capa 4: copia el contenido del directorio actual al directorio /app
COPY . /app

# Capa 5: ejecuta un comando de terminal
CMD ["echo", "Hello World"]
