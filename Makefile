# CraftProtocol Makefile

DOCS = docs
PACKAGE = .

.PHONY: default

default: build

package:
	cd $(PACKAGE)/ && python setup.py sdist

documentation:
	cd $(DOCS)/ && make html

build: clean package documentation

install: package
	yes | pip install --user $(PACKAGE)/dist/*

clean:
	rm -rf $(PACKAGE)/dist/ $(PACKAGE)/MANIFEST
	rm -rf $(DOCS)/build/
	rm -rf pylint.log
	cd $(PACKAGE)/ && python setup.py clean

uninstall:
	yes | pip uninstall CraftProtocol

all: build install
