# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'iYoRoy的小站文档'
copyright = '2019 - 2023, KaguraiYoRoy'
author = 'KaguraiYoRoy'
html_baseurl = 'https://docs.iyoroy.cn/'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['recommonmark',
    'sphinx_markdown_tables',
    'sphinx.ext.githubpages'
    ]

templates_path = ['_templates']
exclude_patterns = []

language = 'zh_CN'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_copy_source = False
html_context = {
    'display_github': True,
    'github_user': 'KaguraiYoRoy',
    'github_repo': 'docs',
    'github_version': 'src/source/'
}

source_parsers = {
    '.md': 'recommonmark.parser.CommonMarkParser',
}

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
# html_logo = '_static/VertillusionNew_.png'

source_suffix = {'.rst': 'restructuredtext','.md': 'markdown'}