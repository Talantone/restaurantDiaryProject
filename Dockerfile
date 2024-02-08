FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt .
COPY .env .
COPY .env.dev .
RUN pip3 install -r requirements.txt
COPY . .