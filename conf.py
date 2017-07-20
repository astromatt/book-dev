#!/usr/bin/env python3

import sys
import os
import subprocess
import datetime


sys.path.append(os.path.abspath('.'))

project = 'DevOps Workshop'
author = 'Matt Harasymczuk'

extensions = [
    'sphinx.ext.todo',
    '_bin.toggle_code_block',
]

def get_version():
    shell = subprocess.Popen('git log -1 --format="%h"', stdout=subprocess.PIPE, shell=True)
    return '{sha1}, {date:%Y-%m-%d}'.format(
        sha1=shell.stdout.read().decode().replace('\n', ''),
        date=datetime.date.today(),
    )

language = 'pl'
copyright = '2012-{date:%Y}, Matt Harasymczuk <matt@astrotech.io>'.format(date=datetime.date.today())
master_doc = 'index'
exclude_patterns = ['Thumbs.db', '.DS_Store', 'README.rst']
pygments_style = 'vs'
todo_include_todos = False
today_fmt = '%Y-%m-%d'
highlight_language = 'python3'
source_suffix = ['.rst']

version = get_version()
release = get_version()


html_theme = 'sphinx_rtd_theme'
#html_theme_path = ['../_themes']
html_static_path = ['_static']
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
    (master_doc, 'DevOpsWorkshop.tex', 'DevOps Workshop', 'Matt Harasymczuk', 'manual'),
]

man_pages = [
    (master_doc, 'devopsworkshop', 'DevOps Workshop', [author], 1)
]

texinfo_documents = [
    (master_doc, 'DevOpsWorkshop', 'DevOps Workshop', author, 'DevOpsWorkshop', 'DevOps Workshop', 'Miscellaneous'),
]
