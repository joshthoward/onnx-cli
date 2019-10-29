def pull_cmd(args):
    """
    """
    raise NotImplementedError("TODO: ")


def push_cmd(args):
    """
    """
    raise NotImplementedError("TODO: ")


def build_cmd(args):
    """
    """
    raise NotImplementedError("TODO: ")


def import_cmd(args):
    """
    """
    raise NotImplementedError("TODO: ")


def export_cmd(args):
    """
    """
    raise NotImplementedError("TODO: ")


def config_cmd(args):
    """
    """
    raise NotImplementedError("TODO: ")


def remote_cmd(args):
    """
    remote = Remote()
    """

    subcmd_lkp = {
        "ls": remote_ls_cmd,
        "rm": remote_rm_cmd,
        "add": remote_add_cmd,
    }

    subcmd = subcmd_lkp[args.subcommand]
    subcmd("", args)


def remote_ls_cmd(remote, args):
    """
    print(remote)
    """
    raise NotImplementedError("TODO: ")


def remote_rm_cmd(remote, args):
    """
    remote.rm(args.remote)
    """
    raise NotImplementedError("TODO: ")


def remote_add_cmd(remote, args):
    """
    remote.add(args.remote, args.url)
    """
    raise NotImplementedError("TODO: ")


def ls_cmd(args):
    """
    """
    raise NotImplementedError("TODO: ")


def rm_cmd(args):
    """
    """
    raise NotImplementedError("TODO: ")
