
test:
	docker-compose run --rm notebook sh -c "python3 -m coverage run --rcfile=.coveragerc -m unittest discover && coverage report"

lint:
	docker-compose run --rm notebook sh -c "flake8"
