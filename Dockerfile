FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app
COPY requirements.txt /app/
RUN pip install --upgrade pip setuptools wheel \
 && pip install -r requirements.txt

COPY . /app

ENV PORT=8080
EXPOSE 8080
CMD ["gunicorn","-w","2","-k","gthread","-b","0.0.0.0:8080","app:app"]