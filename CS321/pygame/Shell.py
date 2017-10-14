Python 3.5.2 (default, Nov 17 2016, 17:05:23) 
[GCC 5.4.0 20160609] on linux
Type "copyright", "credits" or "license()" for more information.
>>> 
=================== RESTART: /home/kimn9/CS321/Testfile.py ===================
hello world
>>> 
=================== RESTART: /home/kimn9/CS321/Testfile.py ===================
>>> run RPG.py
SyntaxError: invalid syntax
>>> run RPG
SyntaxError: invalid syntax
>>> 
>>> python
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    python
NameError: name 'python' is not defined
>>> cd
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    cd
NameError: name 'cd' is not defined
>>> RPG
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    RPG
NameError: name 'RPG' is not defined
>>> /path/to/interpreter
SyntaxError: invalid syntax
>>> ch,od
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    ch,od
NameError: name 'ch' is not defined
>>> chmod
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    chmod
NameError: name 'chmod' is not defined
>>> chmod +x RPG.py
SyntaxError: invalid syntax
>>> python RPG.py
SyntaxError: invalid syntax
>>> 
