include .env .env.dev
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

run_docker_prod:
	export $(shell sed 's/=.*//' .env)
	docker-compose build && docker-compose up

run_docker_dev:
	export $(shell sed 's/=.*//' .env.dev)
	docker-compose build && docker-compose up

.DEFAULT_GOAL := run_prod



















