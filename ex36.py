exec 'print "Hello"'


print """
this is a backslash \\
this is a single-quote \'
this is a double-quote \"
this is a bell \ahehe
this is a backspacess\b
this is a formfeed\fheheh
this is a newline\nhaha
this is a carriage\rhahahahahah!!!!!
this is a tab\thehehehe!!!
this is a vertical tab\vhohohoohoh~~~
"""


a = lambda y: y**y

print a(10)

assert True, "True!"

a = 2

if a == 2:
    raise ValueError("Nooooooo!!!")
