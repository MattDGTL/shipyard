FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install Flask docker

EXPOSE 8765

CMD ["python", "app.py"]