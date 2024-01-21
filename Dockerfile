FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
COPY .env /code/
COPY .env.dev /code/
RUN pip3 install -r requirements.txt
COPY . /code/