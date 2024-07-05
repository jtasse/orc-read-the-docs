# conf.py

import os
import sys
from sphinxcontrib.openapi import OpenApiParser
import yaml

sys.path.insert(0, os.path.abspath('.'))

project = 'My Project'
author = 'My Name'
release = '0.1'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'myst_parser',
    'sphinxcontrib.openapi'
]

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# Register the OpenAPI YAML parser
def setup(app):
    app.add_source_suffix('.yaml', 'yaml')
    app.add_source_parser(OpenApiParser)
