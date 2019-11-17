import argparse
import sys

from .commands import convert
from . import __version__

cmd_lkp = {
    "convert": convert.handler
}


def main():
    """Entrypoint for the ONNX CLI
    """
    # Parse command line arguments
    parser = argparse.ArgumentParser(
        prog="onnx",
        description="A Command Line Interface for interacting with ONNX models",
        epilog="test\n")

    parser.add_argument("-v", "--version", action="store_true",
        help="Print version information and quit")

    # Subcommands
    subparsers = parser.add_subparsers(dest="subcommand")

    convert_parser = subparsers.add_parser("convert",
        help="Convert a model from an external format to the ONNX format")
    convert_parser.add_argument("-f", "--framework", type=str,
        choices=convert.framework_lkp.keys(),
        help="The source model framework")
    convert_parser.add_argument("path", type=str,
        help="The path to the source model")

    args = parser.parse_args()
    if args.version:
        print(__version__)
        return 0

    try:
        cmd = cmd_lkp[args.subcommand]
    except KeyError:
        print("Subcommand required")
        return 1

    cmd(args)


if __name__ == "__main__":
    sys.exit(main())
