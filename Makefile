book:
	@sphinx-build -j4 -b html . _docs/

slides:
	@sphinx-build -j4 -b html slides/ _slides/

help:
	@sphinx-build -M help help help

clean:
	-rm -fr _book/
	-rm -fr _slides/
