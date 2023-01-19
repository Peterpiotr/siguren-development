import os
import re
import shutil
import sys
from pathlib import Path

import docutils
import sphinx
from sphinx.ext import graphviz
from sphinx.util import logging


# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Lumache'
copyright = '2021, Graziella'
author = 'Graziella'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    # Custom Odoo theme
    'odoo_theme',
]



intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']


# -- Options for EPUB output
epub_show_urls = 'footnote'

# -------------------------------------------------------------------------------------------------------------------------

#=== Options for HTML output ===#

html_theme = 'odoo_theme'


# The paths that contain custom themes, relative to this directory.
html_theme_path = ['extensions']