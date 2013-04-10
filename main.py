"""
Problem Statement:
I always forget the boilerplate code to use when creating a standalone, 
executable python module.  Additionally, I'd like to know why this boilerplate
code works like it does.  This example explains what's happening.


Technical Background:

Simplified sequence of module execution by Python interpreter:

1. interpreter defines "special" variables for the module, including __name__

    sets __name__ = "__main__" if run directly by interpreter 
    sets __name__ = main if imported

    Note: if you start the interpreter and print __name__ you'll notice that 
        it's also __main__ in that case.

2. execute all code in file, including imports 


Tests:
    To test the __main__ path execute this module directly with the python
    interpreter
        
        > python main.py

    To test the alternative path start the python interactive interpreter
    and execute the following:

        >>> import main


References: 
    http://stackoverflow.com/questions/419163/what-does-if-name-main-do/419185#419185
    http://ibiblio.org/g2swap/byteofpython/read/module-name.html
"""

if __name__ == "__main__":
    print "(__name__ == %s) Executing as a standalone, executable module" % __name__
else:
    print "(__name__ == %s) Executing as an importable module" % __name__
