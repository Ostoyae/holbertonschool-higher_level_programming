# 0x02. Python - import & modules

## What I should learn from this project

* Why Python programming is awesome (don’t forget to tweet today, with the hashtag #pythoniscool :))
* How to import functions from another file
* How to use imported functions
* How to create a module
* How to use the built-in function `dir()`
* How to prevent code in your script from being executed when imported
* How to use command line arguments with your Python programs


## Tasks

### [0-add](./0-add.py)

Write a program that imports the function `def add(a, b):` from the file `add_0.py` and prints the result of the addition `1 + 2 = 3`


* You have to use `print` function with string format to display integers
* You have to assign:


* the value `1` to a variable called `a` 
* the value `2` to a variable called `b`
* and use those two variables as arguments when calling the functions `add` and `print`

* `a` and `b` must be define in 2 different lines: `a = 1` and another `b = 2`
* Your program should print: `&lt;a value&gt; + &lt;b value&gt; = &lt;add(a, b) value&gt;` followed with a new line
* You can only use the word `add_0` once in your code
* You are not allowed to use `*` for importing or `__import__`
* Your code should not be executed when imported - by using `__import__`, like the example below

