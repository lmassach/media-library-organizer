"""Organizes the media library."""
import argparse
import logging
import logging.handlers
import os
import sys
from .config import load_config, write_default_config

MODULE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_CONFIG_FILE = os.path.join(MODULE_DIR, "medialiborg.json")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)  # TODO examples in epilog?
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-c", "--config", metavar="PATH",
                       default=DEFAULT_CONFIG_FILE,
                       help="The configuration file, default medialiborg.json"
                            " in the module directory.")
    group.add_argument("--write-default-config", metavar="PATH",
                       help="Write the default configuration to the given file"
                            " and exit.")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-v", "--verbose", action="store_const",
                       dest="loglevel", const=logging.INFO,
                       default=logging.WARNING, help="Print more messages.")
    group.add_argument("--debug", action="store_const", dest="loglevel",
                       const=logging.DEBUG, help="Print debug messages.")
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

    # Write default config
    if args.write_default_config is not None:
        write_default_config(args.write_default_config)
        sys.exit(0)

    # Load configuration
    cfg = load_config(args.config)

    # TODO
