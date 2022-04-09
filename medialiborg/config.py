"""Configuration loader for medialiborg."""
import json
import logging

_LOGGER = logging.getLogger(__name__)

DEFAULT_CONFIG = {
    # TODO
}


def load_config(file_path: str):
    """Loads a configuration file and returns a dictionary."""
    _LOGGER.debug("Opening config file %r", file_path)
    with open(file_path) as ifs:
        _LOGGER.debug("Parsing config file %r", file_path)
        config = json.load(ifs)
    config = DEFAULT_CONFIG | config
    _LOGGER.info("Loaded config file %r", file_path)
    return config


def write_default_config(file_path: str):
    """Creates a file with the default configuration."""
    _LOGGER.debug("Writing default config to %r", file_path)
    with open(file_path) as ofs:
        json.dump(DEFAULT_CONFIG, ofs)
    _LOGGER.info("Written default config to %r", file_path)
