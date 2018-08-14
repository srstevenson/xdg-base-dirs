test:
	pipenv run python setup.py test

format:
	pipenv run yapf -i xdg.py test/*.py

.PHONY: format test
