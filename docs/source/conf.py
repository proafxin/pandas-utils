# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import sys
import tomllib
from os.path import abspath, dirname, join

cwd = dirname(abspath(__file__))
root = join(cwd, "../..")

sys.path.insert(0, root)

toml_file = join(root, "pyproject.toml")

with open(toml_file, "rb") as f:
    data = tomllib.load(f)
    version = data.get("tool")["poetry"]["version"]


release = version

project = "Pandas Extras"
copyright = "2023, Masum Billal"
author = "Masum Billal"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
]

templates_path = ["_templates"]
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "furo"

html_theme_options = {}
html_context = {"default_mode": "dark"}

html_static_path = []
