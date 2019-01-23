author = 'Matt Harasymczuk'
email = 'matt@astrotech.io'
project = 'DevOps and CI/CD wtih Docker'
description = "Matt Harasymczuk's DevOps and CI/CD wtih Docker"

extensions = [
    # 'sphinx.ext.doctest',
    'sphinx.ext.todo',
    # 'sphinx.ext.imgmath',
    # 'sphinx.ext.autosectionlabel',
    # 'sphinx.ext.viewcode',
    # 'sphinx.ext.coverage',
    # 'sphinx.ext.githubpages',
    # 'sphinx.ext.autodoc',
    # 'sphinx.ext.intersphinx',
    # 'sphinx.ext.graphviz',
    'sphinxcontrib.bibtex',
    # 'sphinxjp.themes.revealjs',
]

todo_emit_warnings = False
todo_include_todos = True

exclude_patterns = []


# -----------------------------------------------------------------------------
# Standard book config
# -----------------------------------------------------------------------------

import datetime
import os
import re
import subprocess
import sys


numfig_format = {
    'section': 'Sect. %s.',
    'figure': 'Fig. %s.',
    'table': 'Tab. %s.',
    'code-block': 'Code Listing %s.',
}

html_theme = 'sphinx_rtd_theme'
language = 'en'
source_directory = '.'
master_doc = 'index'
highlight_language = 'python3'
pygments_style = 'vs'
numfig = True
templates_path = ['_templates']
source_suffix = ['.rst']
imgmath_image_format = 'svg'
today_fmt = '%Y-%m-%d'
project_slug = re.sub(r'[\W]+', '', project)
sha1 = subprocess.Popen('git log -1 --format="%h"', stdout=subprocess.PIPE, shell=True).stdout.read().decode().replace('\n', '')
version = '#{sha1}, {date:%Y-%m-%d}'.format(sha1=sha1, date=datetime.date.today())
release = '#{sha1}, {date:%Y-%m-%d}'.format(sha1=sha1, date=datetime.date.today())
copyright = '{year}, {author} <{email}>'.format(
    year=datetime.date.today().year,
    author=author,
    email=email,
)

exclude_patterns = exclude_patterns + [
    '.*',
    'venv*',
    'virtualenv*',
    '_extensions',
    '_img',
    '_slides',
    '_static',
    '_themes',
    '_tmp',
    '**.ipynb_checkpoints',
    'README.rst'
]

extensions_dir = os.path.join(os.path.dirname(__file__), '', '_extensions')
sys.path.append(extensions_dir)

html_theme_path = ['_themes']
html_static_path = ['_static']
html_favicon = '_static/favicon.png'
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
