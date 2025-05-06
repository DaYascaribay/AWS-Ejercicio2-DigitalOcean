# Usa la imagen base de Python
FROM python:3.8

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos del proyecto al contenedor
COPY . .

# Instala las dependencias
RUN pip install -r requirements.txt

# Expone el puerto 8081
EXPOSE 8081

# Ejecuta la aplicación Flask
CMD ["python", "app.py"]
