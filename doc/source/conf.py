# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html



# -- Project information -----------------------------------------------------

project = 'Nino-hist'
copyright = '2020, Nino'
author = 'Nino'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
# 
# Select nbsphinx and, if needed, other Sphinx extensions:
extensions = [
	'sphinx.ext.autodoc',
    'nbsphinx',
    'sphinx.ext.mathjax',
    'sphinx.ext.napoleon'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', '**.ipynb_checkpoints', 'Thumbs.db', '.DS_Store', '.env']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Solve Sphinx error:
# master file /home/docs/checkouts/readthedocs.org/user_builds/nino-hist/checkouts/latest/doc/source/contents.rst not found
master_doc = 'index'

# Latex support
latex_engine = 'xelatex'
# latex_elements = {}
latex_documents = [
    (master_doc, 'Nino-hist.tex', 'Nino-hist',
     'Author: Nino', 'manual', True),
]

