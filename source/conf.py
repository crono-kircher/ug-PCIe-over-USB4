# Configuration file for the Sphinx documentation builder.

import os, sys

sys.path.append(os.path.abspath("./_ext"))

# -- Project information

project = 'PCIe-to-USB4 adapter - User Guide'
copyright = '2023, cronologic GmbH & Co. KG'
author = 'cronologic GmbH & Co. KG'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output
html_theme = 'sphinx_rtd_theme'

# latex customization
latex_engine = 'xelatex'
latex_elements = {
    "fontpkg" : r"""
    \setmainfont{TeX Gyre Schola}
    \setsansfont{TeX Gyre Heros}
    \setmonofont{Fira Code}
    """,
    # "preamble": r"\usepackage{cronologicug}"
}

numfig = True
numfig_format = {
    "figure":"Fig. %s:"
}
numfig_secnum_depth = 0