#!/usr/bin/env python3

from datetime import datetime, timezone
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

print('\n')

SECOND = 1
MINUTE = 60 * SECOND

last = run('git log -1 --format="%ad" --date=iso', shell=True, capture_output=True).stdout.strip().decode()
last = datetime.strptime(last, '%Y-%m-%d %H:%M:%S %z')
print('Last commit:', last)

delta = datetime.now(tz=timezone.utc) - last
min = delta.total_seconds() / MINUTE
min = round(min)

print(f'Since: {min}m')
