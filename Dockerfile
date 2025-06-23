FROM python:3.13-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier tout le contenu du projet (backend + Front-end)
COPY . .

# Installer les dépendances
RUN pip install --no-cache-dir -r Backend/requirements.txt

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

EXPOSE 8000

CMD ["sh", "-c", "python Backend/manage.py makemigrations && \
                  python Backend/manage.py migrate && \
                  echo \"from django.contrib.auth import get_user_model; \
                  User = get_user_model(); \
                User.objects.filter(username='superuser').exists() or \
                User.objects.create_superuser('superuser', 'admin@gmail.com', 'superuser123')\" | python Backend/manage.py shell && \
                python Backend/manage.py runserver 0.0.0.0:8000"]
