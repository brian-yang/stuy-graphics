SCRIPT = script.mdl

test: $(SCRIPT) lex.py main.py matrix.py mdl.py display.py draw.py gmath.py yacc.py
	python main.py $(SCRIPT)

clean:
	rm -f *pyc *out parsetab.py *~

clear:
	rm -f *pyc *out parsetab.py *ppm *png
