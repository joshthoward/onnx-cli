# onnx-cli

## Usage 

```
A command line interface for interacting with ONNX models
usage: onnx [-h] [-v] {pull,push,build,import,export,config,remote,ls,rm} ...

A Command Line Interface for interacting with ONNX models

positional arguments:
  {pull,push,build,import,export,config,remote,ls,rm}
    pull                Pull model from a remote registry
    push                Push model to a remote registry
    build               Build a model from an external framework
    import              Import model to the local registry
    export              Export model from the local registry
    config              Set configuration options
    remote              Configure remote registries
    ls                  List models from the local registry
    rm                  Remove model from the local registry

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         Print version information and quit
```
