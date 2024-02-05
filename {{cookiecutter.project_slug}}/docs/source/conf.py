import os
import sys

from sphinx_pyproject import SphinxConfig

config = SphinxConfig("../../pyproject.toml", globalns=globals())
sys.path.insert(0, os.path.abspath("../.."))
