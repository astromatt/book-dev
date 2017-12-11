#!/usr/bin/env python3
import datetime
import subprocess
import sys
import os

sys.path.append(os.path.abspath('.'))

author = 'Matt Harasymczuk'
copyright = '2017-{date:%Y}, Matt Harasymczuk <matt.harasymczuk@esa.int>'.format(date=datetime.date.today())
description = 'DevOps workshop'
description_slug = description.replace(' ', '-')

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.viewcode',
    '_bin.toggle_code_block',
]

language = 'en'
master_doc = 'index'
today_fmt = '%Y-%m-%d'
source_suffix = ['.rst']
imgmath_image_format = 'svg'
exclude = [
    'README.rst',
]

todo_emit_warnings = False
todo_include_todos = True

numfig = True
numfig_format = {
    'section': 'Sect. %s.',
    'figure': 'Fig. %s.',
    'table': 'Tab. %s.',
    'code-block': 'Code Listing %s.',
}


def get_version():
    shell = subprocess.Popen('git log -1 --format="%h"', stdout=subprocess.PIPE, shell=True)
    return '{sha1}, {date:%Y-%m-%d}'.format(
        sha1=shell.stdout.read().decode().replace('\n', ''),
        date=datetime.date.today(),
    )


version = get_version()
release = get_version()

highlight_language = 'python3'
pygments_style = 'sphinx'
html_theme = 'sphinx_rtd_theme'
html_show_sphinx = False
htmlhelp_basename = description

latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '10pt',
    'figure_align': 'htbp',

    # Fix for: LaTeX Backend Fails with Citations In Figure Captions
    'preamble': r'''
        \usepackage{etoolbox}
        \AtBeginEnvironment{figure}{\renewcommand{\phantomsection}{}}
    '''
}

latex_documents = [
    (master_doc, 'document.tex', description, author, 'manual'),
]

man_pages = [
    (master_doc, description_slug, description, [author], 1)
]

texinfo_documents = [
    (master_doc, description_slug, description, author, description_slug, description, 'Miscellaneous'),
]