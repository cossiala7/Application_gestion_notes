FROM python:3.10-slim

WORKDIR /app

COPY Backend/ /app/

RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

EXPOSE 8000

CMD ["sh", "-c", "    python manage.py makemigrations &&     python manage.py migrate &&     echo \"from django.contrib.auth import get_user_model;           User = get_user_model();           User.objects.filter(username='superuser').exists() or           User.objects.create_superuser('superuser', 'admin@example.com', 'superuser123')\" | python manage.py shell &&     python manage.py runserver 0.0.0.0:8000"]
