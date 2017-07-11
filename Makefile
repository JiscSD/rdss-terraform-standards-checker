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

.PHONY: deps* lint
