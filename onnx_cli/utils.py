import re

def write_model(model, path):
    """
    """
    with open(path, "wb") as f:
        f.write(model)


def parse_name(name):
    regex = r"^(.*)/([^/]*):?(.*)$"
    match = re.match(regex, name)

    remote, name, tag = match.groups()

    if tag == "":
        tag = "latest"

    return remote, name, tag
