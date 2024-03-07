# Configuration file for the Sphinx documentation builder.

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join("..", "{{cookiecutter.project_slug.replace('-', '_')}}")))


# -- Project information

project = "{{cookiecutter.project_slug}}"
copyright = "{{cookiecutter.full_name}}"
author = "{{cookiecutter.full_name}}"
__version__ = "0.0.0"
version = __version__
release = __version__

# -- General configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.extlinks",
    "sphinx.ext.mathjax",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx_mdinclude",
]


templates_path = ["_templates"]

autodoc_default_options = {
    "members": True,
    "undoc-members": True,
    "private-members": True,
}

# -- Options for HTML output

html_theme = "sphinx_rtd_theme"

# -- Options for EPUB output
epub_show_urls = "footnote"


# -- Automatically run apidoc to generate rst from code
# https://github.com/readthedocs/readthedocs.org/issues/1139
def run_apidoc(_):
    from sphinx.ext.apidoc import main

    sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
    cur_dir = os.path.abspath(os.path.dirname(__file__))

    module_dir = os.path.join(cur_dir, "..", "..", "{{cookiecutter.project_slug.replace('-', '_')}}")
    output_dir = os.path.join(cur_dir, "api")
    main(["-f", "-o", output_dir, module_dir])


def setup(app):
    app.connect("builder-inited", run_apidoc)
