import argparse
import logging
import sys

from onnx_cli import __version__
from onnx_cli.subcommand_support import *


logging_lkp = {
    "critical": logging.CRITICAL,
    "error": logging.ERROR,
    "warning": logging.WARNING,
    "info": logging.INFO,
    "debug": logging.DEBUG
}


command_lkp = {
    "build": build_handler,
    "run": run_handler,
    "import": import_handler,
    "export": export_handler
}


def main():
    """Entrypoint for the ONNX CLI
    """
    # Parse command line arguments
    parser = argparse.ArgumentParser(
        prog="onnx",
        description="A Command Line Interface for interacting with ONNX models",
        epilog="This project is not in production")

    # Global arguments
    parser.add_argument("-v", "--version", action="store_true",
                        help="Print version information and quit")
    parser.add_argument("-l", "--logging", default="warning",
                        choices=logging_lkp.keys(),
                        help="Set logging level for command")
    subparsers = parser.add_subparsers(dest="command")

    build_parser = subparsers.add_parser("build")
    build_parser.add_argument("-f", "--from", 
        choices=["coreml", "keras", "lightgbm", "sklearn", "sparkml", "tensorflow", "xgboost"],
        help="Set model type from")

    run_parser = subparsers.add_parser("run")
    import_parser = subparsers.add_parser("import")
    export_parser = subparsers.add_parser("export")

    args = parser.parse_args()
    if args.version:
        print(__version__)
        sys.exit(0)

    # Configure logger
    logging.basicConfig(level=logging_lkp[args.logging],
                        format="%(asctime)s:%(levelname)s:%(message)s")
    logger = logging.getLogger("onnx")
    logger.debug("Initialized logger")

    # Execute subcommand
    command = command_lkp[args.command]
    logger.debug("Executing the {0} subcommand".format(args.command))
    command(args)


if __name__ == "__main__":
    main()
