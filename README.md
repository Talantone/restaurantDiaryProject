# Second project for ThinkEasy

# launch

Use the `make requirements` command or `pip3 install -r requirements.txt` before running.

Makefile(`make`) and docker(`docker-compose up`).
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
