author = 'Matt Harasymczuk'
email = 'matt@astrotech.io'
project = 'Software Engineering'
description = "Matt Harasymczuk's Software Engineering"
language = 'en'
todo_emit_warnings = False
todo_include_todos = True

numfig_format = {
    'section': 'Section %s.',
    'figure': 'Figure %s.',
    'table': 'Table %s.',
    'code-block': 'Listing %s.',
}

extensions = [
    'sphinxcontrib.bibtex',
    'sphinx.ext.todo',
    # 'sphinx.ext.doctest',
    # 'sphinx.ext.imgmath',
    # 'sphinx.ext.autosectionlabel',
    # 'sphinx.ext.viewcode',
    # 'sphinx.ext.coverage',
    # 'sphinx.ext.githubpages',
    # 'sphinx.ext.autodoc',
    # 'sphinx.ext.intersphinx',
    # 'sphinx.ext.graphviz',
    # 'sphinxjp.themes.revealjs',
]


# -----------------------------------------------------------------------------
# Standard book config
# -----------------------------------------------------------------------------

import re
import sys
from datetime import datetime
from subprocess import run


def abs_path(relative_path):
    from os.path import dirname, abspath, join
    base_dir = dirname(abspath(__file__))
    return join(base_dir, relative_path)


needs_sphinx = '2.2'

mathjax_path = 'https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/latest.js?config=TeX-MML-AM_CHTML'
mathjax_config = {
    'extensions': ['tex2jax.js'],
    'jax': ['input/TeX', 'output/HTML-CSS'],
}

html_theme = 'sphinx_rtd_theme'

exclude_patterns = [
    'ecosystem/*',
    'process/*',
    'ci-cd/*',

    '.*',
    '.venv-*',
    '*/_slides',
    '*/_static',
    '*/_themes',
    '*/_tmp',
    '*/_template.rst',
    '*/contrib/*',
    '*/solution/*',
    '**.ipynb_checkpoints',
    'README.rst',
    'TODO.rst',
]

suppress_warnings = ['toc.secnum']
source_directory = abs_path('.')
master_doc = 'index'
highlight_language = 'python3'
pygments_style = 'borland'
numfig = True
templates_path = [abs_path('_templates')]
source_suffix = ['.rst']
imgmath_image_format = 'svg'
today_fmt = '%Y-%m-%d'

project_slug = re.sub(r'[\W]+', '', project)
sha1 = run('git log -1 --format="%h"', shell=True, capture_output=True).stdout.strip().decode()
now = datetime.now()
year = now.year
today = now.strftime('%Y-%m-%d')

version = f'#{sha1}, {today}'
release = f'#{sha1}, {today}'
copyright = f'{year}, {author} <{email}>'

extensions_dir = abs_path('_extensions')
sys.path.append(extensions_dir)

htmlhelp_basename = project
html_theme_path = [abs_path('_themes')]
html_static_path = [abs_path('_static')]
html_favicon = abs_path('_static/favicon.png')
html_sidebars = {'sidebar': ['localtoc.html', 'sourcelink.html', 'searchbox.html']}
html_show_sphinx = False
html_context = {
    'css_files': [
        '_static/screen.css',
        '_static/print.css',
    ],
    'script_files': [
        '_static/jquery.min.js',
        '_static/onload.js',
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
