NAME = xdg

lint:
	flake8 $(NAME).py
	pylint -r n $(NAME).py

format:
	yapf -i $(NAME).py

upload: lint
	python setup.py sdist bdist_wheel
	twine upload -s dist/*

clean:
	$(RM) -r $(wildcard *.egg-info *.pyc) build dist

.PHONY: clean format lint upload
