# -*- coding: utf-8 -*-
"""Sphinx configuration."""
import os
import sys
from typing import Any, Dict, List

sys.path.insert(0, os.path.abspath(os.path.join("..", "..")))

import e_lims  # noqa E402

# -- General configuration ---------------------------------------------
extensions = [
    "sphinx.ext.autodoc",
    "sphinx_autodoc_typehints",
    "sphinx.ext.doctest",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx.ext.coverage",
    "sphinx.ext.viewcode",
    "sphinxcontrib.mermaid",
]

templates_path = ["_templates"]
source_suffix = ".rst"
master_doc = "index"

# General information about the project.
project = "e-lims"
package = "e_lims"
author = e_lims.__author__
copy_right = f"2022, {author}"
version = e_lims.__version__
release = e_lims.__version__
language = "en"
exclude_patterns: List[Any] = []
pygments_style = "sphinx"
todo_include_todos = True


# -- Options for HTML output -------------------------------------------
html_theme = "sphinx_rtd_theme"

# -- Options for HTMLHelp output ---------------------------------------
htmlhelp_basename = "e_limsdoc"

# -- Options for LaTeX output ------------------------------------------
latex_elements: Dict[Any, Any] = {}

latex_documents = [
    (master_doc, "e_lims.tex", f"{project} Documentation", author, "manual"),
]


# -- Options for manual page output ------------------------------------
man_pages = [(master_doc, "e_lims", f"{project} Documentation", [author], 1)]

# -- Options for Texinfo output ----------------------------------------
texinfo_documents = [
    (
        master_doc,
        "e_lims",
        f"{project} Documentation",
        author,
        "e_lims",
        """Python Boilerplate contains all the boilerplate you need to create a Python package with Poetry.""",
        "Miscellaneous",
    ),
]

intersphinx_mapping = {"python": ("https://docs.python.org/3/", None)}
set_type_checking_flag = True
always_document_param_types = True
