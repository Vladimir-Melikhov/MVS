# Используем Python 3.10 (как в твоих pyc файлах)
FROM python:3.10-slim

# Устанавливаем переменные окружения для Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Устанавливаем рабочую директорию
WORKDIR /app

# Устанавливаем системные зависимости (нужны для Postgres и Pillow)
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    netcat-openbsd \
    && apt-get clean

# Устанавливаем зависимости Python
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Копируем проект
COPY . .

# Создаем папки для статики и медиа
RUN mkdir -p /app/staticfiles /app/media

# Скрипт запуска (entrypoint)
COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]