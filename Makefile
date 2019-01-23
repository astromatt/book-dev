book = /tmp/devops-book/
slides = /tmp/devops-slides/

book:
	@rm -fr $(book) && clear && sphinx-build -j11 -b html . $(book)

slides:
	@rm -fr $(book) && clear && sphinx-build -j11 -b html _slides/ $(slides)

help:
	@sphinx-build -M help help help

clean:
	-rm -fr $(book)
	-rm -fr $(slides)
