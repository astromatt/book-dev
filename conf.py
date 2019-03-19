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

from datetime import datetime
import os
import re
import subprocess
import sys


html_theme = 'sphinx_rtd_theme'

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
    '*/_template.rst',
    '*/contrib/*',
    '*/solution/*',
    '*/solutions/*',
    '**.ipynb_checkpoints',
    'README.rst',
    'TODO.rst',
]

numfig_format = {
    'section': 'Sect. %s.',
    'figure': 'Fig. %s.',
    'table': 'Tab. %s.',
    'code-block': 'Code Listing %s.',
}

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
now = datetime.now()
year = now.year
today = now.strftime('%Y-%m-%d')

version = f'#{sha1}, {today}'
release = f'#{sha1}, {today}'
copyright = f'{year}, {author} <{email}>'

extensions_dir = os.path.join(os.path.dirname(__file__), '', '_extensions')
sys.path.append(extensions_dir)

htmlhelp_basename = project
html_theme_path = ['_themes']
html_static_path = ['_static']
html_favicon = '_static/favicon.png'
html_sidebars = {'sidebar': ['localtoc.html', 'sourcelink.html', 'searchbox.html']}
html_show_sphinx = False
html_context = {
    'css_files': [
        '_static/theme-overrides.css',
    ],
}

latex_documents = [(master_doc, f'{project_slug}.tex', project, author, 'manual')]
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
