import sys; sys.path.append('..')
from conf import *

project = 'Jira with Atlassian Ecosystem'
author = 'Matt Harasymczuk'
email = 'matt@astrotech.io'
language = 'en'

todo_emit_warnings = True
todo_include_todos = True

html_favicon = '../_static/favicon.png'
html_static_path = ['../_static']
html_context.update({
        'css_files': ['_static/light.css', '_static/print.css'],
        'script_files': ['_static/jquery.min.js', '_static/onload.js']})
