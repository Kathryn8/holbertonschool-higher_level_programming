#m = 6-square 	# Imanually enter the module name
#c = Square	# Class name
#f = my_print	# function name
PYTHON=python3
PYTHONC=$(PYTHON) -c
PYCODESTYLE=pycodestyle

all: 0 1 2 3 4

run:
	$(PYTHON) $(t)-main.py 	# t="task number", entered from command line

testall: ptest mtest ctest cftest ftest

ptest:
	$(PYCODESTYLE) $(m).py

mtest:
	$(PYTHON) -c 'print(__import__("$(m)").__doc__)'

ctest:
	@echo "------------------------------------------------"
	@echo "Check comment in class $(c) from the module $(m)"
#	@$(PYTHONC) 'print("Check OK") if len(__import__("$(m)").$(c).__doc__) > 10 else print("No comment found or comment too short")'
	var="@$(PYTHONC) 'len(__import__(\"$(m)\").$(c).__doc__)'"
	echo $(var)
	@echo "------------------------------------------------"

ftest:
	$(PYTHON) -c 'print(__import__("$(m)").$(f).__doc__)'

cftest:
	$(PYTHON) -c 'print(__import__("$(m)").$(c).$(f).__doc__)'

jon:
	@echo $(j)

0:
	@$(MAKE) j=kathryn jon

1:
	$(MAKE) m=1-square c=Square ctest
#	$(MAKE) m=1-square mtest

#0: testall m=0-square c=Square

clean:
	rm -rf __pycache__
