from setuptools import setup

REQUIREMENTS = ["pyparrot", "opencv-python-headless"]

# DO NOT EDIT BELOW THIS LINE
DEV_REQUIREMENTS = [
    "pre-commit",
    "black",
    "flake8",
    "flake8-docstrings",
    "isort",
    "pep8-naming",
]

setup(
    name="parrot",
    version="0.0.1",
    description="Control Parrot Bebop Drone with Python using Hand Gestures",
    author=["Ali Albustami", "Aya Haubsh"],
    python_requires="==3.6.13",
    packages=["src", "tests"],
    install_requires=REQUIREMENTS + DEV_REQUIREMENTS,
    license="MIT",
)
