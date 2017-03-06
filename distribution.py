"""
distribution.py
Author: <your name here>
Credit: <list sources used, if any>

Assignment:

Write and submit a Python program (distribution.py) that computes and displays 
the distribution of characters in a given sample of text.

Output of your program should look like this:

Please enter a string of text (the bigger the better): The rain in Spain stays mainly in the plain.
The distribution of characters in "The rain in Spain stays mainly in the plain." is:
iiiiii
nnnnnn
aaaaa
sss
ttt
ee
hh
ll
pp
yy
m
r

Notice about this example:

* The text: 'The rain ... plain' is provided by the user as input to your program.
* Uppercase characters are converted to lowercase
* Spaces and punctuation marks are ignored completely.
* Characters that are more common appear first in the list.
* Where the same number of characters occur, the lines are ordered alphabetically. 
  For example, in the printout above, the letters e, h, l, p and y both occur twice 
  in the text and they are listed in the output in alphabetical order.
* Letters that do not occur in the text are not listed in the output at all.
"""

letter=input("Please enter a string of text (the bigger the better): ")
print("The distribution of characters in \"" +letter+ "\". is:")

print((letter).count('a'))
print((letter).count('b'))
print((letter).count('c'))
print((letter).count('d'))
print((letter).count('e'))
print((letter).count('f'))
print((letter).count('g'))
print((letter).count('h'))
print((letter).count('i'))
print((letter).count('j'))
print((letter).count('k'))
print((letter).count('l'))
print((letter).count('m'))
print((letter).count('o'))
print((letter).count('p'))
print((letter).count('q'))
print((letter).count('r'))
print((letter).count('s'))
print((letter).count('t'))
print((letter).count('v'))
print((letter).count('w'))
print((letter).count('x'))
print((letter).count('y'))
print((letter).count('z'))