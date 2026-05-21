<<<<<<< HEAD
FROM python:3.10-slim

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt

EXPOSE 80
=======
FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .
EXPOSE 5000

>>>>>>> 77b998713556ff72574aa0e4f81282f8718998f3
CMD ["python", "app.py"]