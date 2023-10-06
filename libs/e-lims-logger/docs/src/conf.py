# -*- coding: utf-8 -*-
"""Sphinx configuration."""
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join('..', '..')))

import src  # noqa: E402

# -- General configuration ---------------------------------------------
extensions = [
    "sphinx.ext.autodoc",
    "sphinx_autodoc_typehints",
    "sphinx.ext.doctest",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx.ext.coverage",
    "sphinx.ext.viewcode",
]

templates_path = ["_templates"]
source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}
master_doc = "index"

# General information about the project.
project = 'e-lims-logger'
package = "e_lims_logger"
author = src.__author__
copyright = '2023, {}'.format(author)
version = '0.0.0'
release = '0.0.0'
language = 'en'
exclude_patterns = []
pygments_style = "sphinx"
todo_include_todos = True


# -- Options for HTML output -------------------------------------------
html_theme = "sphinx_rtd_theme"

# -- Options for HTMLHelp output ---------------------------------------
htmlhelp_basename = 'e_lims_logger_doc'

# -- Options for LaTeX output ------------------------------------------
latex_elements = {}

latex_documents = [
    (master_doc, 'e_lims.tex',
     '{} Documentation'.format(project),
     author, 'manual'),
]


# -- Options for manual page output ------------------------------------
man_pages = [
    (master_doc, 'e_lims',
     '{} Documentation'.format(project),
     [author], 1)
]

# -- Options for Texinfo output ----------------------------------------
texinfo_documents = [
    (master_doc, 'e_lims',
     '{} Documentation'.format(project),
     author,
     'e_lims',
     """e_lims_logger Cookiecutter Template.""",
     'Miscellaneous'),
]

intersphinx_mapping = {"python": ("https://docs.python.org/3/", None)}
set_type_checking_flag = True
always_document_param_types = True