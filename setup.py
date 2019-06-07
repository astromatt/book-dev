#!/usr/bin/env python3

from os import makedirs
from os.path import dirname, abspath, join, basename
from shlex import split
from shutil import rmtree
from subprocess import run


FORMAT = 'html'

sourcedir = dirname(abspath(__file__))
project_name = basename(sourcedir)
outputdir = join('/tmp/', project_name)

rmtree(outputdir, ignore_errors=True)
makedirs(outputdir, exist_ok=True)
run('clear')

cmd = split(f'sphinx-build -a -E -j auto --color -b {FORMAT} {sourcedir} {outputdir}')
run(cmd)
