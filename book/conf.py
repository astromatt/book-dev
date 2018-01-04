#!/usr/bin/env python3
import sys
import os
import datetime
import subprocess

BASE_DIR = os.path.dirname(__file__)
sys.path.append(os.path.join(BASE_DIR, '..', '_extensions'))

author = 'Matt Harasymczuk'
email = 'matt@astrotech.io'
project = 'DevOps and Development Tools Ecosystem'
description = 'Matt Harasymczuk\'s DevOps and Development Tools Ecosystem'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.viewcode',
    'toggle_code_block',
]

todo_emit_warnings = False
todo_include_todos = True
html_theme = 'sphinx_rtd_theme'
pygments_style = 'vs'

language = 'en'
numfig_format = {
    'section': 'Sect. %s.',
    'figure': 'Fig. %s.',
    'table': 'Tab. %s.',
    'code-block': 'Code Listing %s.',
}

# -----------------------------------------------------------------------------
# Unified book config
# -----------------------------------------------------------------------------
highlight_language = 'python3'
numfig = True
templates_path = ['_templates']
master_doc = 'index'
source_suffix = ['.rst']
imgmath_image_format = 'svg'
today_fmt = '%Y-%m-%d'
project_slug = project.lower().replace(' ', '-')
sha1 = subprocess.Popen('git log -1 --format="%h"', stdout=subprocess.PIPE, shell=True).stdout.read().decode().replace('\n', '')
version = '#{sha1}, {date:%Y-%m-%d}'.format(sha1=sha1, date=datetime.date.today())
release = '#{sha1}, {date:%Y-%m-%d}'.format(sha1=sha1, date=datetime.date.today())
copyright = '{year}, {author} <{email}>'.format(
    year=datetime.date.today().year,
    author=author,
    email=email,
)

exclude = ['README.rst']
exclude_patterns = ['_build', '_book', '_slides', 'img', '_themes', 'slides', 'README.rst', '*/_template.rst']

html_theme_path = ['_themes']
html_static_path = []
html_sidebars = {'sidebar': ['localtoc.html', 'sourcelink.html', 'searchbox.html']}
html_show_sphinx = False
htmlhelp_basename = project

latex_documents = [(master_doc, '{0}.tex'.format(project_slug), project, author, 'manual')]
latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '10pt',
    'figure_align': 'htbp',

    # Fix for: LaTeX Backend Fails with Citations In Figure Captions
    'preamble': r"""
        \usepackage{etoolbox}
        \AtBeginEnvironment{figure}{\renewcommand{\phantomsection}{}}
    """
}

epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright
epub_exclude_files = ['search.html']


man_pages = [
    (master_doc, project_slug, project, [author], 1)
]

texinfo_documents = [
  (master_doc, project_slug, project, author, project, '', 'Miscellaneous'),
]