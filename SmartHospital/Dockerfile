# Dockerfile
FROM python:3.12-slim

# Prevent Python from writing .pyc files and buffering stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /SmartHospital

# system deps for pillow, etc. (keep minimal)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install
COPY requirements.txt /SmartHospital/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . /SmartHospital/

# Create folder for static files
RUN mkdir -p /vol/static /vol/media

# Add entrypoint and make executable
COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

EXPOSE 8000

ENTRYPOINT ["/entrypoint.sh"]
CMD ["gunicorn", "SmartHospital.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]
