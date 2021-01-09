project = 'The Software Engineering'
author = 'Matt Harasymczuk'
email = 'book-dev@astrotech.io'

language = 'en'
html_theme = 'sphinx_rtd_theme'
html_baseurl = 'https://dev.astrotech.io'

todo_emit_warnings = False
todo_include_todos = True

extensions = [
    # 'sphinx.ext.autosectionlabel',
    'sphinx.ext.duration',
    # 'sphinx.ext.doctest',
    # 'sphinx.ext.extlinks',
    # 'sphinx.ext.graphviz',
    'sphinx.ext.mathjax',
    'sphinx.ext.todo',
    # 'sphinx.ext.viewcode',
    'sphinxcontrib.bibtex',
    # 'recommonmark',
    # 'nbsphinx'
]

suppress_warnings = [
    # 'app.add_node',
    # 'app.add_directive',
    # 'app.add_role',
    # 'app.add_generic_role',
    # 'app.add_source_parser',
    # 'download.not_readable',
    # 'image.not_readable',
    'ref.term',
    # 'ref.ref',
    # 'ref.numref',
    # 'ref.keyword',
    # 'ref.option',
    # 'ref.citation',
    # 'ref.footnote',
    # 'ref.doc',
    # 'ref.python',
    # 'misc.highlighting_failure',
    # 'toc.circular',
    'toc.secnum',
    # 'epub.unknown_project_files',
    'autosectionlabel.*',
]

html_static_path = [
    '_static',
]

# article - For articles in scientific journals, presentations, short reports,
#           Program documentation, invitations, etc
# proc    - A class for proceedings based on the article class.
# minimal - Is as small as it can get. It only sets a page size and a base font.
#           It is mainly used for debugging purposes.
# report  - For longer reports containing several chapters, small books, thesis, etc
# book    - For real books
# slides  - For slides. The class uses big sans serif letters.
# memoir  - For changing sensibly the output of the document.
#           It is based on the book class, but you can create
#           any kind of document with it (1)
# letter  - For writing letters.
# beamer  - For writing presentations (see LaTeX/Presentations).
latex_documentclass = 'report'

if 'recommonmark' in extensions:
    def setup(app):
        from recommonmark.transform import AutoStructify
        app.add_config_value('recommonmark_config', {
            'enable_eval_rst': True,
        }, True)
        app.add_transform(AutoStructify)


# -- Standard book config -----------------------------------------------------

import os
import re
import subprocess
import sys
from datetime import date

needs_sphinx = '3.3'
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

sys.path.insert(0, os.path.abspath('_extensions'))

# 0 - sequence number of image in whole document
# 1 - sequence number of image in header level 1 (only if :numbered: option is present at toctree directive)
# 2 - sequence number of image in header level 2
#       will use x.1, x.2, … if located directly under a header level 1,
#       will use 1, 2, … if at the document level
# etc...
numfig_secnum_depth = 1
numfig = True
smartquotes = False
numfig_format = {
    'section': 'Section %s.',
    'figure': 'Figure %s.',
    'table': 'Table %s.',
    'code-block': 'Code %s.'}

project_slug = re.sub(r'[\W]+', '', project)
sha1 = subprocess.run('git log -1 --format="%h"', stdout=subprocess.PIPE, shell=True, encoding='utf-8').stdout.strip()
year = date.today().year
today = date.today().strftime('%Y-%m-%d')

version = f'#{sha1}, {today}'
release = f'#{sha1}, {today}'
copyright = f'{year}, CC-BY-SA-4.0, {author} <{email}>, last update: {today}'

exclude_patterns = [
    '.*',
    'venv*',
    'virtualenv*',
    '.venv*',
    '.virtualenv*',
    '_build',
    '_extensions',
    '_img',
    '_slides',
    '_i18n',
    '_static',
    '_themes',
    '_tmp',
    '_contrib',
    '__ecosystem',
    '__process',
    '_layouts',
    '_slides',
    '_contrib',
    '_solution',
    '_assignment',
    '_template.rst',
    '*/_slides/**',
    '*/_contrib',
    '*/_solution',
    '*/_assignment',
    '*/_template.rst',
    '*.ipynb_checkpoints',
    'README.rst',
    'TODO.rst',
    '**/_TODO.rst',
    'Thumbs.db',
    '.DS_Store',
]

master_doc = 'index'
templates_path = ['_templates']
highlight_language = 'python3'
pygments_style = 'borland'
autodoc_typehints = "description"
autosectionlabel_maxdepth = 4
autosectionlabel_prefix_document = True


if 'nbsphinx' in extensions:
    # https://nbsphinx.readthedocs.io/en/latest/usage.html
    nbsphinx_input_prompt = 'In [%s]:'
    nbsphinx_output_prompt = 'Out [%s]:'
    nbsphinx_execute = 'always'
    nbsphinx_allow_errors = True
    nbsphinx_timeout = 5
    nbsphinx_execute_arguments = [
        "--InlineBackend.figure_formats={'svg'}",  # 'pdf'
        "--InlineBackend.rc={'figure.dpi': 96}"]
    suppress_warnings += ['nbsphinx',
                          'nbsphinx.localfile',
                          'nbsphinx.gallery',
                          'nbsphinx.thumbnail',
                          'nbsphinx.notebooktitle',
                          'nbsphinx.ipywidgets']


if 'sphinxcontrib.bibtex' in extensions:
    bibtex_bibliography_header = ".. rubric:: References"
    bibtex_footbibliography_header = bibtex_bibliography_header
    bibtex_default_style = 'alpha'
    bibtex_bibfiles = [
        '_references/bibliography.bib',
        '_references/images.bib',
        '_references/video.bib',
        'agile/_references/bibliography.bib',
        'agile/_references/images.bib',
        'agile/_references/video.bib',
        'architecture/_references/bibliography.bib',
        'docker/_references/bibliography.bib',
        'git/_references/bibliography.bib',
        'jenkins/_references/bibliography.bib',
        'jira/_references/bibliography.bib',
        'linux/_references/bibliography.bib']


if 'sphinx.ext.extlinks' in extensions:
    extlinks = {'isbn': ('https://e-isbn.pl/IsbnWeb/start/search.html?szukaj_fraza=%s', 'ISBN: ')}


if 'sphinx.ext.doctest' in extensions:
    import doctest
    trim_doctest_flags = False
    # doctest_global_cleanup = """"""
    # doctest_default_flags = doctest.ELLIPSIS | doctest.IGNORE_EXCEPTION_DETAIL | doctest.NORMALIZE_WHITESPACE
    # doctest_default_flags = doctest.FAIL_FAST | doctest.IGNORE_EXCEPTION_DETAIL

html_show_sphinx = False
html_use_smartypants = False
html_search_language = language
html_add_permalinks = '¶'
html_theme_path = ['_themes']
html_secnumber_suffix = '. '
html_title = project
html_favicon = '_static/favicon.png'
html_context = {}
html_copy_source = False
html_style = '_static/light.css'

if html_theme == 'sphinx_rtd_theme':
    html_context.update({
        'css_files': ['_static/light.css', '_static/print.css'],
        'script_files': ['_static/jquery.min.js', '_static/onload.js']})

if html_theme == 'thesis':
    html_context.update({
        'css_files': ['_static/theme-overrides.css'],
        'script_files': []})


if 'sphinx.ext.mathjax' in extensions:
    imgmath_image_format = 'png'
    imgmath_latex = 'latex'
    # mathjax_path = '_static/mathjax.js'
    mathjax_path = 'https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js'
    mathjax_config = {
        'extensions': ['tex2jax.js'],
        'jax': ['input/TeX', 'output/HTML-CSS']}
    if 'script_files' in html_context:
        html_context['script_files'] += [mathjax_path]
    else:
        html_context['script_files'] = [mathjax_path]


latex_documents = [('index', f'{project_slug}.tex', project, author, latex_documentclass)]
latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '10pt',
    'figure_align': 'H',  # 'htbp',

    # Fix for: LaTeX Backend Fails with Citations In Figure Captions
    'preamble': r"""
        \usepackage{float}
        \usepackage{etoolbox}
        \AtBeginEnvironment{figure}{\renewcommand{\phantomsection}{}}
    """}

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
