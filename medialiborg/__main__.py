"""Organizes the media library."""
import argparse
import logging
import logging.handlers
import os
from .config import load_config, write_default_config

MODULE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_CONFIG_FILE = os.path.join(MODULE_DIR, "medialiborg.json")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)  # TODO examples in epilog?
    # TODO
    parser.add_argument("-c", "--config", metavar="PATH",
                        default=DEFAULT_CONFIG_FILE,
                        help="The configuration file, default medialiborg.json"
                             " in the module directory.")
    parser.add_argument("-v", "--verbose", action="store_const",
                        dest="loglevel", const=logging.WARNING,
                        default=logging.DEBUG, help="Print debug messages.")
    parser.add_argument("-l", "--log", help="Log file (default stderr).")
    args = parser.parse_args()

    # Configure logging
    if args.log:
        f = logging.Formatter("%(asctime)s %(levelname)s %(name)s %(message)s",
                              "%Y/%m/%d %H:%M:%S%z")
        h = logging.handlers.RotatingFileHandler(
            args.log, maxBytes=1048576, backupCount=3, encoding='utf8',
            errors='replace')
        h.setFormatter(f)
    else:
        f = logging.Formatter("%(asctime)s %(levelname)s %(name)s %(message)s",
                              "%H:%M:%S%z")
        h = logging.StreamHandler()
        h.setFormatter(f)
    logging.basicConfig(level=args.loglevel, handlers=[h])
    logger = logging.getLogger("main")

    # Load configuration
    cfg = load_config(args.config)

    # TODO
