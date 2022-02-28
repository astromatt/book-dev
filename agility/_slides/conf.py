#!/usr/bin/env python3
import datetime
import os
import re
import subprocess
import sys


project = 'Workshop Agile'
project_slug = re.sub(r'[\W]+', '', project)
description = 'Workshop Agile'
author = 'Matt Harasymczuk'
copyright = '2017-{year}, Matt Harasymczuk <matt@astrotech.io>'.format(year=datetime.date.today().year)

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

language = 'en'
master_doc = 'index'
today_fmt = '%Y-%m-%d'
source_suffix = ['.rst']
imgmath_image_format = 'svg'
exclude = ['README.rst']

todo_emit_warnings = True
todo_include_todos = False

numfig = True
numfig_format = {
    'section': 'Sect. %s',
    'figure': 'Fig. %s',
    'table': 'Tab. %s',
    'code-block': 'List. %s',
}


def get_version():
    shell = subprocess.Popen('git log -1 --format="%h"', stdout=subprocess.PIPE, shell=True)
    return '{sha1}, {date:%Y-%m-%d}'.format(
        sha1=shell.stdout.read().decode().replace('\n', ''),
        date=datetime.date.today(),
    )


version = get_version()
release = get_version()

extensions_dir = os.path.join(os.path.dirname(__file__), '..', '_extensions')
sys.path.append(extensions_dir)

# highlight_language = 'python3'
# pygments_style = 'sphinx'
html_theme = 'revealjs'
html_use_index = False
html_show_sphinx = False
htmlhelp_basename = project

html_theme_options = {
    # Set the lang attribute of the html tag. Defaults to "ja"
    "lang": "en",

    # The "normal" size of the presentation, aspect ratio will be preserved
    # when the presentation is scaled to fit different resolutions
    "width": 960,
    "height": 700,

    # Factor of the display size that should remain empty around the content
    "margin": 0.1,

    # Bounds for smallest/largest possible scale to apply to content
    "min_scale": 0.2,
    "max_scale": 1.0,

    # Display controls in the bottom right corner
    "controls": True,

    # Display a presentation progress bar
    "progress": True,

    # Push each slide change to the browser history
    "history": True,

    # Enable keyboard shortcuts for navigation
    "keyboard": True,

    # Enable the slide overview mode
    "overview": True,

    # Vertical centring of _slides
    "center": True,

    # Enables touch navigation on devices with touch input
    "touch": True,

    # Loop the presentation
    "loop": False,

    # Change the presentation direction to be RTL
    "rtl": False,

    # Turns fragments on and off globally
    "fragments": True,

    # Number of milliseconds between automatically proceeding to the
    # next slide, disabled when set to 0, this value can be overwritten
    # by using a data-autoslide attribute on your _slides
    "auto_slide": 0,

    # Enable slide navigation via mouse wheel
    "mouse_wheel": False,

    # Apply a 3D roll to links on hover
    "rolling_links": True,

    # Opens links in an iframe preview overlay
    "preview_links": False,

    # Theme (black/white/league/beige/sky/night/serif/simple/solarized)
    "theme": "black",

    # Transition style (default(=convex)/none/fade/slide/concave/zoom)
    "transition": "none",

    # Transition speed (default/fast/slow)
    "transition_speed": "default",

    # Transition style for full page slide backgrounds (default(=convex)/none/fade/slide/concave/zoom)
    "background_transition": "default",

    # Display the page number of the current slide
    "slide_number": False,

    # Flags if the presentation is running in an embedded mode,
    # i.e. contained within a limited portion of the screen
    "embedded": False,

    # Stop auto-sliding after user input
    "auto_slide_stoppable": True,

    # Hides the address bar on mobile devices
    "hide_address_bar": True,

    # Parallax background image
    # CSS syntax, e.g. "a.jpg"
    #"parallax_background_image": '_static/bg.jpg',

    # Parallax background size
    # CSS syntax, e.g. "3000px 2000px"
    #"parallax_background_size": '2000px 900px',

    # Focuses body when page changes visibility
    # to ensure keyboard shortcuts work
    "focus_body_on_page_visibility_change": True,

    # Number of _slides away from the current that are visible
    "view_distance": 3,
}