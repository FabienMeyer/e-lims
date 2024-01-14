"""Sphinx configuration."""
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join("..", "..")))

import src

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
    ".rst": "restructuredtext",
    ".txt": "markdown",
    ".md": "markdown",
}
master_doc = "index"

# General information about the project.
project = "e-lims-utils"
package = "e-lims-utils"
author = src.__author__
copyright = f"2024, {author}"
version = src.__version__
release = src.__version__
language = "en"
exclude_patterns = []
pygments_style = "sphinx"
todo_include_todos = True

# -- Options for HTML output -------------------------------------------
html_theme = "furo"

# -- Options for HTMLHelp output ---------------------------------------
htmlhelp_basename = f"{project}-doc"

# -- Options for LaTeX output ------------------------------------------
latex_elements = {}

latex_documents = [
    (master_doc, f"{project}.tex", f"{project} Documentation", author, "manual"),
]

# -- Options for manual page output ------------------------------------
man_pages = [(master_doc, project, f"{project} Documentation", [author], 1)]

# -- Options for Texinfo output ----------------------------------------
texinfo_documents = [
    (master_doc, project, f"{project} Documentation", author, project, """e-lims-utils Cookiecutter Template.""", "Miscellaneous"),
]

intersphinx_mapping = {"python": ("https://docs.python.org/3/", None)}
set_type_checking_flag = True
always_document_param_types = True
