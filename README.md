# Pandas Extras

[![Build, test with Tox and deploy](https://github.com/proafxin/pd-extras/actions/workflows/build_test.yaml/badge.svg)](https://github.com/proafxin/pd-extras/actions/workflows/build_test.yaml)
[![codecov](https://codecov.io/gh/proafxin/pd-extras/graph/badge.svg?token=AQA0IJY4N1)](https://codecov.io/gh/proafxin/pd-extras)
[![Documentation Status](https://readthedocs.org/projects/pd-extras/badge/?version=latest)](https://pd-extras.readthedocs.io/en/latest/?badge=latest)

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pd-extras?logo=python&logoColor=yellow&style=for-the-badge)
![PyPI - Version](https://img.shields.io/pypi/v/pd-extras?logo=python&logoColor=yellow&style=for-the-badge)
![Docker Image Version (tag)](https://img.shields.io/docker/v/_/postgres/latest?arch=amd64&style=for-the-badge&logo=postgresql&logoColor=white&label=Postgresql)
![Docker Image Version (tag)](https://img.shields.io/docker/v/_/mysql/latest?arch=amd64&style=for-the-badge&logo=mysql&logoColor=white&label=mysql)

Some functions on top of pandas.

## Install Environment

For local development:

- Run `python -m pip install -U pip` and `pip install -U pip poetry`
- Run `poetry install`. If you are facing issues installing `mysqlclient` or `psycopg2` on Ubuntu, it's because you are missing some libraries. Please check their pages. Usually for `psycopg2`, it's `libpq-dev` and for `mysqlclient`, it's `python3-dev default-libmysqlclient-dev build-essential`. Check the pages for more specific and accurate commands.

## Testing

Run `docker compose up` then `tox`. Obviously you need docker and tox installed.

## Generate Documentation Source Files

You should not have to do this but in case you want to generate the source ReStructuredText files yourself, here is how. Skip to the next section to simply generate html documentation locally.

Change to docs directory `cd docs/`. Run `sphinx-quickstart`. Choose `y` when it asks to seperate build and source directories.

Change to `docs/source` directory. In `conf.py`, add the following lines at the start of the script.

```python
import os
import sys

sys.path.insert(0, os.path.abspath("../.."))
```

and save it. Add `"sphinx.ext.autodoc",` to the `extensions` list. Run `python -m pip install -U sphinx_rtd_theme` and set `html_theme = "sphinx_rtd_theme"` (or whatever theme you want).

In `index.rst`, add `modules` to toctree. The structure should look like this:

```markdown
.. toctree::
:maxdepth: 2
:caption: Contents:

modules
```

Run the following to generate the source files.

```markdown
poetry install --with docs
poetry run sphinx-apidoc -f -o source/ ../ ../tests/
```

## Generating HTML Documentation

Change to `docs/` using `cd ..` then run `.\make clean` and `.\make html`. Output should be built with no errors or warnings. You will get the html documenation in `docs/build/html` directory. Open `index.html`.
