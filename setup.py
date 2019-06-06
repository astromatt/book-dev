#!/usr/bin/env python3

from os import makedirs
from os.path import dirname, abspath, join, basename
from shlex import split
from shutil import rmtree
from subprocess import run


OUTPUT_DIR = '/tmp/'
FORMAT = 'html'
THREADS = 11
VENV = '/src/book/.venv-3.7.3'


sourcedir = dirname(abspath(__file__))
project_name = basename(sourcedir)
outputdir = join(OUTPUT_DIR, project_name)
sphinx_build = join(VENV, 'bin', 'sphinx-build')

rmtree(outputdir, ignore_errors=True)
makedirs(outputdir, exist_ok=True)

run('clear')

cmd = split(f'{sphinx_build} -j {THREADS} -b {FORMAT} {sourcedir} {outputdir}')
run(cmd)
