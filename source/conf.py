# Configuration file for the Sphinx documentation builder.
# import os, sys
# sys.path.insert(0, os.path.abspath(".."))

# -- Project information
project = 'PCIe-over-USB4 Manual'
copyright = '2023, cronologic'
author = 'Max Kircher'

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

# -- pdf build using rinoh
rinoh_documents = [{
    'doc':'index',
    'target':'man-PCIe-over-USB4-rinoh',
    'template':r'.\pdftemplate.rtt',
}]

# latex_toplevel_sectioning = 'section'


