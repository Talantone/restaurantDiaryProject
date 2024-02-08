FROM alpine
FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt .
COPY .env .
COPY .env.dev .
RUN pip3 install -r requirements.txt
COPY . .
RUN python3 manage.py makemigrations; \
    python3 manage.py migrate
RUN useradd -ms /bin/bash appuser
RUN addgroup appgroup && adduser appuser appgroup
RUN chown appuser:appgroup /code/manage.py
RUN chmod +x /code/manage.py
USER appuser

CMD [ "python3", "/code/manage.py", "runserver", "0.0.0.0:8000" ]