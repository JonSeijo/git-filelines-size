# filelines-measurer
Show stats graphs of the lines of a file in time. Useful only if file was tracked by git.


## Requirements:

- git
- matplotlib  (for graph drawing)
`` sudo apt-get install python3-matplotlib ``

Or see http://matplotlib.org/users/installing.html


## Instructions

Execute in console

`` python3 filelines.py filepath`` 

Where 'filepath' is the path (relative or absolute) of the file you want to measure.


### Custom horizontal line

If you want a fixed horizontal line (maybe to compare the lines with a limit),
you can pass an optional value **--y_line** followed by a number

`` python3 filelines.py filepath --y_line 300``

(This will draw an horizontal line at y=300)


![alt text][image1]
[image1]: https://raw.githubusercontent.com/JonSeijo/filelines-measurer/master/img/example.png "filelines measuring example"


### Troubleshooting
*fatal: XXX: 'XXX' is outside repository*

- If the file to measure is in an outside repository, you **need** to specify the path of the git repository where the file is located.
Use --gitdir path/to/git/repo

`` python3 filelines.py filepath --gitdir path/to/git/repo `` 


#### Python2

It should also work with python 2.x, but I will not guarantee it

`` python filelines.py filename`` 
