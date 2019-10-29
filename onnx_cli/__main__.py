import argparse
import logging
import sys

from onnx_cli import __version__
from onnx_cli.cmd import *


cmd_lkp = {
    "pull": pull_cmd,
    "push": push_cmd,
    "build": build_cmd,
    "import": import_cmd,
    "export": export_cmd,
    "config": config_cmd,
    "remote": remote_cmd,
    "ls": ls_cmd,
    "rm": rm_cmd
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
    subparsers = parser.add_subparsers(dest="command")

    pull_parser = subparsers.add_parser("pull",
        help="Pull model from a remote registry")
    pull_parser.add_argument("name", type=str,
        help="The fully qualified name of the model")

    push_parser = subparsers.add_parser("push",
        help="Push model to a remote registry")
    push_parser.add_argument("name", type=str,
        help="The fully qualified name of the model")

    build_parser = subparsers.add_parser("build",
        help="Build a model from an external framework")
    build_parser.add_argument("name", type=str,
        help="The fully qualified name of the model")
    build_parser.add_argument("path", type=str,
        help="The path to the external framework model")

    import_parser = subparsers.add_parser("import",
        help="Import model to the local registry")
    import_parser.add_argument("path", type=str,
        help="The path to the model")
    import_parser.add_argument("name", type=str,
        help="The fully qualified name of the model")

    export_parser = subparsers.add_parser("export",
        help="Export model from the local registry")
    export_parser.add_argument("name", type=str,
        help="The fully qualified name of the model")
    export_parser.add_argument("path", type=str,
        help="The path to the model")

    config_parser = subparsers.add_parser("config",
        help="Set configuration options")
    config_parser.add_argument("key", type=str,
        help="Option key")
    config_parser.add_argument("value", type=str,
        help="Option value")

    remote_parser = subparsers.add_parser("remote",
        help="Configure remote registries")
    remote_subparser = remote_parser.add_subparsers(dest="subcommand")
    remote_ls_parser = remote_subparser.add_parser("ls",
        help="List remote registries")
    remote_rm_parser = remote_subparser.add_parser("rm",
        help="Remove remote registry")
    remote_rm_parser.add_argument("remote", type=str,
        help="Name of the remote registry")
    remote_add_parser = remote_subparser.add_parser("add",
        help="Add remote registry")
    remote_add_parser.add_argument("remote", type=str,
        help="Name of the remote registry")
    remote_add_parser.add_argument("url", type=str,
        help="URL of the remote registry")

    ls_parser = subparsers.add_parser("ls",
        help="List models from the local registry")

    rm_parser = subparsers.add_parser("rm",
        help="Remove model from the local registry")

    args = parser.parse_args()
    if args.version:
        print(__version__)
        return 0

    cmd = cmd_lkp[args.command]
    cmd(args)


if __name__ == "__main__":
    sys.exit(main())
