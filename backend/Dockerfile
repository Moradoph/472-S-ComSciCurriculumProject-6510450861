FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    libmariadb-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

    
COPY . .
    
RUN chmod +x wait-for-it.sh

RUN pip install --no-cache-dir -r requirement.txt

EXPOSE 8000

CMD ["./wait-for-it.sh", "db:3306", "--", "./wait-for-it.sh", "minio:9000", "--", "sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]