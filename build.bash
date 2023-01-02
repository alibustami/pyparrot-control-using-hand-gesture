#!/usr/bin/env bash

conda env create -f environment.yaml
conda activate parrot-env
python -m pip install --upgrade pip
pip install --upgrade pip setuptools wheel
python -m pip install -e .
pre-commit install
