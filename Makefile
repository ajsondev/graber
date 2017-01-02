build: venv deps develop

venv:
	virtualenv --no-site-packages --python=python3.4 .env
	
deps:
	.env/bin/pip install -r requirements_dev.txt

develop:
	.env/bin/python setup.py develop

flake:
	flake8 graber

flake_verbose:
	flake8 graber --show-pep8

clean:
	find -name '*.pyc' -delete
	find -name '*.swp' -delete

upload:
	python setup.py sdist upload

.PHONY: all build venv flake test clean doc
