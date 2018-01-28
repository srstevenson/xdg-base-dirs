check: lint test

lint:
	mypy --ignore-missing-imports xdg.py test_xdg.py
	flake8 xdg.py test_xdg.py
	pylint -r n -s n xdg.py test_xdg.py

test:
	pytest test_xdg.py

format:
	yapf -i xdg.py test_xdg.py

upload: check
	python setup.py sdist bdist_wheel
	twine upload -s dist/*

clean:
	$(RM) -r $(wildcard *.egg-info *.pyc) build dist

.PHONY: clean format check lint test upload
