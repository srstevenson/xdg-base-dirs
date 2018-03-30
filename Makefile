check: lint test

lint:
	mypy --ignore-missing-imports --strict xdg.py test/*.py
	flake8 xdg.py test/*.py
	pylint -r n -s n xdg.py test/*.py

test:
	python setup.py test

format:
	yapf -i xdg.py test/*.py

upload: check
	python setup.py sdist bdist_wheel
	twine upload -s dist/*.tar.gz
	twine upload -s dist/*.wheel

clean:
	$(RM) -r $(wildcard *.egg-info *.pyc) build dist

.PHONY: clean format check lint test upload
