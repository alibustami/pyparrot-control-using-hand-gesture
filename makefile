virenv:
	conda env create -f environment.yaml


install:
	python -m pip install --upgrade pip && \
	pip install --upgrade pip setuptools wheel && \
	python -m pip install -e . && \
	pre-commit install

test:
	python -m unittest discover tests
