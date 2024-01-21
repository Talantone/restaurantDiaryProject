.PHONY: run_prod

requirements:
	pip3 install -r requirements.txt
run_dev:
	ENV=dev python3 manage.py runserver
run_prod:
    ENV=prod python3 manage.py runserver
run_tests:
	python3 manage.py test .
tests_report:
	ENV=dev coverage run --source='.' ./manage.py test .
	coverage report

.DEFAULT_GOAL := run_prod



















