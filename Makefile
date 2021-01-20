#########################
# DEFAULTS
#########################
GUINICORN_PORT = 8000
GUINICORN_WORKERS = 1
GUINICORN_TIME_OUT = 120
#################################################################################
# GLOBALS                                                                       #
#################################################################################

PROJECT_NAME = Payment-Test
PYTHON_INTERPRETER = python3

#########################
# DEFAULTS
#########################

#################################################################################
# COMMANDS                                                                      #
#################################################################################
clean: .clean-pyc .clean-test


.clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +
	find . -name '.vscode' -exec rm -fr {} +

.clean-test:
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/

deps: 
	$(PYTHON_INTERPRETER) -m pip install -U -r requirement.txt


format:
	set -e
	isort --recursive  --force-single-line-imports app tests
	autoflake --recursive --remove-all-unused-imports --remove-unused-variables --in-place app tests
	black app tests
	isort --recursive app tests

mock_pipeline: lint test_with_coverage


lint:
	set -e
	set -x
	flake8 app tests --exclude=app/core/config.py 
	# isort --recursive --check-only app

test_with_coverage:
	set -e
	set -x
	coverage run -m pytest -p no:warnings ./tests/*


run_server:
	gunicorn --bind 0.0.0.0:8080 runner:app --workers ${GUINICORN_WORKERS} --timeout ${GUINICORN_TIME_OUT} -k uvicorn.workers.UvicornWorker

