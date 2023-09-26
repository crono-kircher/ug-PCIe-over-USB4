# Configuration file for the Sphinx documentation builder.

import os, sys

sys.path.append(os.path.abspath("./_ext"))

# -- Project information

project = 'PCIe-to-USB4 adapter — User Guide'
copyright = ("Creative Commons Attribution-NoDerivatives"
             " 4.0 International License")
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
    "papersize": "a4paper",
    "pointsize": "12pt",
    "fontpkg" : r"""
        \setmainfont{TeX Gyre Schola}
        \setsansfont{Fira Sans}
        \setmonofont{Fira Code}
    """,
    "preamble": r"\usepackage{sphinxcronologic}",
    "fncychap": "",#r"\usepackage[Bjornstrup]{fncychap}",
    "extraclassoptions": r"openany",
    "maketitle": r"\cronofront{../../source/XTDC4_title.pdf}",
    "tableofcontents":"",
    "sphinxsetup": r"""
        TitleColor={rgb}{0.1686,0.4667,0.6941}
    """
}
# latex_toplevel_sectioning = "section" 
latex_theme = "manual" # manual (book class) or howto (article class)
latex_additional_files = ["sphinxcronologic.sty", "extraplaceins.sty"]

numfig = True
numfig_format = {
    "figure":"Fig. %s:",
    "table":"Tab. %s:"
}
numfig_secnum_depth = 0