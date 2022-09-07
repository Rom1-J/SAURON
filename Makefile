VIRTUAL_ENV := venv
PYTHON_PATH := $(VIRTUAL_ENV)/bin/python

BASE := DJANGO_READ_DOT_ENV_FILE=True
MANAGE_PY := $(BASE) $(PYTHON_PATH) manage.py

#######################
# Dev
#######################
.PHONY: run
run:
	$(MANAGE_PY) runserver_plus 0.0.0.0:8000 --keep-meta-shutdown

.PHONY: console
console: shell

.PHONY: shell
shell:
	$(MANAGE_PY) shell

.PHONY: test
test:
	$(BASE) $(PYTHON_PATH) -m pytest $(ARGS)

ifeq (manage,$(firstword $(MAKECMDGOALS)))
  MANAGE_ARGS := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
  $(eval $(MANAGE_ARGS):;@:)
endif
.PHONY: manage
manage:
	$(MANAGE_PY) $(MANAGE_ARGS)

#######################
# Database
#######################
.PHONY: migrations
migrations:
	$(MANAGE_PY) makemigrations

.PHONY: migrate
migrate:
	$(MANAGE_PY) migrate

.PHONY: graph_model
graph_model:
	$(MANAGE_PY) graph_models -a -o models.png

#######################
# Style
#######################
.PHONY: lint
lint:
	$(PYTHON_PATH) -m pylint sauron \
		--load-plugins=pylint_django \
		--django-settings-module=config.settings.local

.PHONY: black
black:
	$(PYTHON_PATH) -m black sauron
	$(PYTHON_PATH) -m black config

.PHONY: type
type:
	$(PYTHON_PATH) -m mypy sauron

.PHONY: style
style: black type lint

.PHONY: pre_commit
pre_commit:
	./$(VIRTUAL_ENV)/bin/pre-commit run --all-files
