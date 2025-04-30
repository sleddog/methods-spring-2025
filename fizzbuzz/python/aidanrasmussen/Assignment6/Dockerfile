FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt app.py ./

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5001

CMD ["python", "app.py"]
