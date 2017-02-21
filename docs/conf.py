#!/usr/bin/env python3

import sys
import os
import shlex
import subprocess
import datetime


project = 'DevOps Workshop'
copyright = '2017, Matt Harasymczuk'
author = 'Matt Harasymczuk'

extensions = [
    'sphinx.ext.todo',
    # 'sphinx.ext.githubpages'
]

def get_version():
    return '{date:%Y-%m-%d}, #{sha1}'.format(
        sha1=subprocess.Popen('git log -1 --format="%h"', stdout=subprocess.PIPE, shell=True).stdout.read().decode().replace('\n', ''),
        date=datetime.date.today(),
    )

language = 'pl'
#templates_path = ['../_templates']
source_suffix = ['.rst']
#source_parsers = {'.md': 'recommonmark.parser.CommonMarkParser'}
master_doc = 'index'
exclude_patterns = ['Thumbs.db', '.DS_Store']
pygments_style = 'vs'
todo_include_todos = True
today_fmt = '%Y-%m-%d'

version = get_version()
release = get_version()


html_theme = 'sphinx_rtd_theme'
#html_theme_path = ['../_themes']
html_static_path = ['../_static']
html_sidebars = {'sidebar': ['localtoc.html', 'sourcelink.html', 'searchbox.html']}
html_show_sphinx = False
htmlhelp_basename = 'DevOpsWorkshop'


latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '10pt',
    # 'preamble': '',
    # 'figure_align': 'htbp',
}

latex_documents = [
    (master_doc, 'DevOpsWorkshop.tex', 'DevOps Workshop Documentation', 'Matt Harasymczuk', 'manual'),
]

man_pages = [
    (master_doc, 'devopsworkshop', 'DevOps Workshop Documentation', [author], 1)
]

texinfo_documents = [
    (master_doc, 'DevOpsWorkshop', 'DevOps Workshop Documentation', author, 'DevOpsWorkshop', 'DevOps Workshop Documentation', 'Miscellaneous'),
]
