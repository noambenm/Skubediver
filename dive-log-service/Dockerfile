# Python 3.11 slim (multi-arch) — good balance of size and compatibility
FROM python:3.11-slim

WORKDIR /app

# Install Python deps first to leverage Docker layer caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the service code
COPY . .

# Best practice for containers running Python services
ENV PYTHONUNBUFFERED=1
EXPOSE 5001

CMD ["python", "main.py"]
