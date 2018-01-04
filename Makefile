book:
    @sphinx-build -j4 -b html book/ _book/

slides:
    @sphinx-build -j4 -b html slides/ _slides/

help:
    @sphinx-build -M help help help

clean:
    -rm -fr _book/
    -rm -fr _slides/
