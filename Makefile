check: lint test

lint:
	pipenv run flake8 xdg.py test/*.py
	pipenv run pylint -r n -s n xdg.py test/*.py

test:
	pipenv run python setup.py test

format:
	pipenv run yapf -i xdg.py test/*.py

upload: check
	pipenv run python setup.py sdist bdist_wheel
	pipenv run twine upload -s dist/*.tar.gz
	pipenv run twine upload -s dist/*.wheel

clean:
	$(RM) -r $(wildcard *.egg-info *.pyc) build dist

.PHONY: clean format check lint test upload
