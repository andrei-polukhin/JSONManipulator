.PHONY: clean clean-test clean-pyc clean-build docs help

clean: clean-build clean-pyc clean-test ## remove all build, test, coverage and Python artifacts


clean-build: ## remove build artifacts
	rm -rf build/
	rm -rf dist/
	rm -rf .eggs/
	find . -name '*.egg-info' -exec rm -rf {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -rf {} +

clean-test: ## remove test and coverage artifacts
	rm -rf .tox/
	rm -f .coverage
	rm -rf htmlcov/

lint: ## check style with flake8
	flake8 JSONManipulator tests

test: ## run tests quickly with the default Python
	pytest -s < testing.txt

test-all: ## run tests on every Python version with tox
	tox < testing.txt

coverage: ## check code coverage quickly with the default Python
	coverage run -m pytest -s > testing.txt
	coverage report -m
	coverage html
	$(BROWSER) htmlcov/index.html

build_docs: ## run sphinx build on docs/ directory
	sphinx-build -b html docs/ docs/_build

docs: ## generate Sphinx HTML documentation, including API docs
	sphinx-apidoc -o docs/ -T JSONManipulator
	$(MAKE) -C docs clean
	$(MAKE) -C docs html
	$(BROWSER) docs/_build/html/index.html

docs_force:
	sphinx-apidoc -o docs/ -T -f JSONManipulator
	$(MAKE) -C docs clean
	$(MAKE) -C docs html
	$(BROWSER) docs/_build/html/index.html

release: clean ## package and upload a release
	python3 setup.py sdist bdist_wheel
	twine upload dist/*

dist: clean ## builds source and wheel package
	python3 setup.py sdist bdist_wheel
	ls -l dist

install: clean ## install the package to the active Python's site-packages
	python setup.py install
