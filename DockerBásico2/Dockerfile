# Imagen base oficial de Python
FROM python:3.12

# Establecer directorio de trabajo
WORKDIR /app

# Copiar archivo de dependencias
COPY requirements.txt .

# Instalar dependencias
RUN pip install -r requirements.txt

# Copiar el resto de los archivos (como app.py)
COPY . .

# Comando para ejecutar la app
CMD ["python", "app.py"]