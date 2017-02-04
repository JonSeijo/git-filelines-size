# filelines-measurer
Show stats graphs of the lines of a file in time. Useful only if file was tracked by git.

## Instructions

*Put filelines.py in any directory inside the repository you want to track*

(Why? Because it need to be in the same repo of the file to get stats of that repo. This is a limitation of git, maybe there is a workaround)

Execute in console

`` python3 filelines.py filename`` 

Where 'filename' is the path (relative or absolute) of the file you want to measure.


## Requirements:

- git
- matplotlib  (for graph drawing)
`` http://matplotlib.org/users/installing.html ``


#### Python2

It should also work with python 2.x, but I will not guarantee it

`` python filelines.py filename`` 
