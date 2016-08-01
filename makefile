DOC_DIR = doc

.PHONY: doc deploy

test: ext
	nosetests -s

ext: core/*.c core/*.h
	python setup.py build_ext --inplace

sdist:
	python setup.py build sdist

doc:
	$(MAKE) -C $(DOC_DIR) html 

deploy: sdist doc
	$(MAKE) -C $(DOC_DIR) deploy
	python setup.py sdist register upload
