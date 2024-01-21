# Second project for ThinkEasy

# launch

Use the `make requirements` command or `pip3 install -r requirements.txt` before running.

Configurate your `.env` and `.env.dev` with something like that for `.env.dev`:
```
SECRET_KEY=your_secret_key
DEBUG=False
ALLOWED_HOSTS=['*']
OWNER_EMAIL=talantoner@gmail.com
SITE_URL=http://localhost:8000
EMAIL_HOST_USER=talantoner@gmail.com
CELERY_BROKER_URL=amqp://guest@localhost:5672//
```
and something like that for `.env`:
```
SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=['*']
OWNER_EMAIL=talantoner@gmail.com
SITE_URL=http://localhost:8000
EMAIL_HOST_USER=talantoner@gmail.com
CELERY_BROKER_URL=amqp://guest@localhost:5672//
```
**Yes, files in the example have only different `DEBUG` option.**

## Makefile(`make`) and docker(`docker-compose up`).  
For Makefile-launch you can use `make run_dev`(to run development server) or `make run_prod` (to run production server)

for docker-compose specify environment with commands:
```
docker-compose build
set -a
source .env.dev //you can use .env or .env.dev file in this command
docker-compose up
```

# testing 
Use command `make run_tests` or `python3 manage.py test .` to run tests
To get test report type `make tests_report` or series of commands `coverage run --source='.' ./manage.py test .` and `coverage report`
