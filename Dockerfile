# Usar una imagen base de Python 3.10
FROM python:3.10

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos de requisitos y el código
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app/
RUN python manage.py migrate

EXPOSE 8000

# Configurar el punto de entrada para Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
