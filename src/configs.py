"""Contains the configs loading finctionality."""
from typing import Any

import yaml


def load(key: str) -> Any:
    """Loads a config value from the config.yaml file.

    Parameters
    ----------
    key : str
        The key of the config value to load.

    Returns
    -------
    Any
        The config value.
    """

    with open("config.yaml") as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
    return config[key]


def load_all() -> dict:
    """Loads all config values from the config.yaml file.

    Returns
    -------
    dict
        A dictionary of all config values.
    """

    with open("config.yaml") as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
    return config
