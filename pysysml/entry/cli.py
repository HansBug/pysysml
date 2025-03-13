from .dispatch import pysysmlcli

# add adding methods here
_DECORATORS = [
]

cli = pysysmlcli
for deco in _DECORATORS:
    cli = deco(cli)
