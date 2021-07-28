%.tex: %.adoc preamble.tex
	asciidoctor-latex -b latex -a preamble=preamble.tex -a skip-front-matter $<

%.pdf: %.tex
	latexmk -pdf $< -outdir=$(shell dirname $@)
	latexmk -c $<
	$(RM) $<
