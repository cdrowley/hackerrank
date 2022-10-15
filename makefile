.PHONY: build clean run 

build:
	python3 -m venv venv; \
	source venv/bin/activate; \
	pip3 install -r requirements.txt;

clean:
	rm -rf venv

run:
	source venv/bin/activate
