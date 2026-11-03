FROM python:3.11-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    tesseract-ocr \
    tesseract-ocr-ara \
    tesseract-ocr-eng \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# نسخ build.py فقط
COPY build.py .

# بناء المشروع كامل
RUN python build.py

# نسخ الملفات المبنية
RUN cp -r ell-hoot-bot/* /app/ && \
    cp -r ell-hoot-bot/.env.example /app/ 2>/dev/null || true

# تثبيت المكتبات
RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONUNBUFFERED=1
ENV DATA_DIR=/app/data
ENV LOGS_DIR=/app/logs

RUN mkdir -p /app/data /app/logs

CMD ["python", "main.py"]
