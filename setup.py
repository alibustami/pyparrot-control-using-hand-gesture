from setuptools import setup

REQUIREMENTS = [
    "pyparrot",
    "opencv-python-headless",
    "mediapipe",
    "untangle",
    "zeroconf",
]

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
    author_email=["alialbustami@gmail.com", "ayahaubsh9@gmail.com"],
    python_requires="==3.6.13",
    packages=["src", "tests"],
    install_requires=REQUIREMENTS + DEV_REQUIREMENTS,
    license="MIT",
    include_package_data=True,
)
