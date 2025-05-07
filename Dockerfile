# Usar imagen base de Python
FROM python:3.8

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos de la aplicación al contenedor
COPY . .

# Instalar las dependencias
RUN pip install -r requirements.txt

# Exponer el puerto
EXPOSE 8080

# Comando para ejecutar la app
CMD ["python", "app.py"]
