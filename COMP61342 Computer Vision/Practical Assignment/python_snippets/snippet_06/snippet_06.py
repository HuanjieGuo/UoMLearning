# snippet_06.py
# -----------------------

"""
Python Code Snippets
Terence Morley, Department of Computer Science,
    The University of Manchester, Nov 2020

Purpose: Access command-line arguments.

Try the following arguments on the command-line. For example,
python3 snippet_05.py one two three four

<None>
1 2 3
Aaa Bbb Ccc
First "Second argument" Third "Testing, testing, 1, 2, 3"
"""

import sys

# How many arguments were supplied? argv[0] is the script name
numArgs = len(sys.argv)
print('\n{} command-line arguments were supplied'.format(numArgs))

# print out the list of arguments
print('\nThe arguments were:')

for i in range(len(sys.argv)):
    print(i, '-', sys.argv[i])

print() # blank line
