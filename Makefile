test:
	pipenv run python setup.py test

format:
	pipenv run yapf -i xdg.py test/*.py

upload: test
	pipenv run python setup.py sdist bdist_wheel
	pipenv run twine upload -s dist/*.tar.gz
	pipenv run twine upload -s dist/*.wheel

clean:
	$(RM) -r $(wildcard *.egg-info *.pyc) build dist

.PHONY: clean format test upload
