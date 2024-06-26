install:
	# install commands
	pip install --upgrade pip && pip install -r requirements.txt
	
format:
	# format code
	black *.py config/*.py crm/*.py

lint:
	# flake8 or pylint
	pylint --disable=R,C,E1101 *.py config/*.py crm/*.py

test:
	# test
	# python -m pytest --cov=mylib tests/*.py

build:
	# docker-compose up --build
	# docker-compose up --build
run:
	# docker run
	# docker run -p 127.0.0.1:8080:8080 b19ef7dfd01b

deploy:
	# deploy on aws ecr
	# aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 355438754535.dkr.ecr.us-east-1.amazonaws.com
	# docker build -t django-crm .
	# docker tag django-crm:latest 355438754535.dkr.ecr.us-east-1.amazonaws.com/django-crm:latest
	# docker push 355438754535.dkr.ecr.us-east-1.amazonaws.com/django-crm:latest

install-local:
	# use this to work with poetry in your local environment
	poetry install --no-root

all: install format lint test deploy

check: format lint

run-dj:
	# python3 manage.py runserver
	python3 manage.py runserver