.PHONY: docs release clean build install test

test: buildenv install
	. a2billing_flask_api_env/bin/activate; python setup.py test

buildenv:
	virtualenv a2billing_flask_api_env
	. a2billing_flask_api_env/bin/activate; pip install -Ur requirements.txt

# assume that the developer already works with virtualenv
# or virtualenv-wrapper
install:
	. a2billing_flask_api_env/bin/activate; python setup.py install

coverage: install
	coverage run --source=a2billing_flask_api setup.py test
	coverage report
	coverage html

docs: buildenv
	$(MAKE) -C docs;

clean:
	rm -rf a2billing_flask_api_env htmlcov

cleanall: clean
	$(MAKE) -C docs clean
