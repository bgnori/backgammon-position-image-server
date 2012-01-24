.PHONY: env build clean freeze develop

env:
	virtualenv --clear mypython;\
	source ./mypython/bin/activate;\
	pip install -r freeze.txt

freeze:
	pip freeze > freeze.txt

#pip install git+ssh://git@github.com:bgnori/bglib.git

develop:
	python setup.py develop
