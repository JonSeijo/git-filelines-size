# filelines-measurer
Show stats graphs of the lines of a file in time. Useful only if file was tracked by git.

## Instructions

Execute in console

`` python3 filelines.py filepath`` 

Where 'filepath' is the path (relative or absolute) of the file you want to measure.

IMPORTANT,
*fatal: XXX: 'XXX' is outside repository*

- If the file to measure is in an outside repository, you **need** to specify the path of the git repository where the file is located.
Use --gitdir path/to/git/repo

`` python3 filelines.py --gitdir path/to/git/repo  filepath`` 


## Requirements:

- git
- matplotlib  (for graph drawing)
`` sudo apt-get install python3-matplotlib ``

Or see http://matplotlib.org/users/installing.html


#### Python2

It should also work with python 2.x, but I will not guarantee it

`` python filelines.py filename`` 
