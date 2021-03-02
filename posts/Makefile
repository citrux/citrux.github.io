%.tex: %.adoc
	asciidoctor-latex -b latex $<

%.pdf: %.tex preamble.tex
	latexmk -pdf $<
	latexmk -c
	$(RM) $<

clean:
	latexmk -C
