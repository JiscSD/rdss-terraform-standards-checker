name:
	@echo $(shell basename $(PWD))

env:
	@virtualenv -p python3 env

deps:
	@pip install -r requirements.txt
	@pre-commit install

deps-update:
	@pip install -r requirements-to-freeze.txt --upgrade
	@pip freeze > requirements.txt

deps-uninstall:
	@pip uninstall -yr requirements.txt
	@pip freeze > requirements.txt

lint:
	@pre-commit run \
		--allow-unstaged-config \
		--all-files \
		--verbose

autopep8:
	@autopep8 . --exclude env --recursive --in-place --pep8-passes 2000 --verbose

autopep8-stats:
	@pep8 --quiet --statistics .

test:
	@pytest

clean:
	@find . -name '__pycache__' | xargs rm -rf

.PHONY: deps* clean lint test autopep8*
