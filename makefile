virenv:
	conda env create -f environment.yaml && \
	source $$(conda info --base)/etc/profile.d/conda.sh && conda activate parrot-env && \


install:
	python -m pip install --upgrade pip && \
	pip install --upgrade pip setuptools wheel && \
	python -m pip install -e . && \
	pre-commit install

test:
	python -m unittest discover tests
