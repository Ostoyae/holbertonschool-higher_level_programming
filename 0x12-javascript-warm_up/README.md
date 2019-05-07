# 0x12. Javascript - Warm up

**Table Of Context**
- [0. First constant, first print](#0-First-constant,-first-print)
- [1. 3 languages](#1-3-languages)
- [2. Arguments](#2-Arguments)
- [3. Value of my argument](#3-Value-of-my-argument)
- [4. Create a sentence](#4-Create-a-sentence)
- [5. An Integer](#5-An-Integer)
- [6. Loop to languages](#6-Loop-to-languages)
- [7. I love C](#7-I-love-C)
- [8. Square](#8-Square)
- [9. Add](#9-Add)
- [10. Factorial](#10-Factorial)
- [11. Second biggest!](#11-Second-biggest!)
- [12. Object](#12-Object)
- [13. Add file](#13-Add-file)

## Tasks


### 0. First constant, first print
File: **[0-javascript_is_amazing.js](0-javascript_is_amazing.js)**

Write a script that prints “Javascript is amazing”:

* You must create a constant variable called `myVar` with the value “Javascript is amazing”
* You must use `console.log(...)` to print all output
* You are not allowed to use `var`

**Repo:**

* GitHub repository: `holbertonschool-higher_level_programming`
* Directory: `0x12-javascript-warm_up`
* File: `0-javascript_is_amazing.js`

Each container will be available 24h max
```
martin@ubuntu:~/0x12$ ./0-javascript_is_amazing.js
Javascript is amazing
martin@ubuntu:~/0x12$
martin@ubuntu:~/0x12$ semistandard ./0-javascript_is_amazing.js
martin@ubuntu:~/0x12$

```



*[top](#0x12-Javascript---Warm-up)*

---


### 1. 3 languages
File: **[1-multi_languages.js](1-multi_languages.js)**

Write a script that prints 3 lines:

* The first line: “C is fun”
* The second line: “Python is cool”
* The third line: “Javascript is amazing”
* You must use `console.log(...)` to print all output
* You are not allowed to use `var`

**Repo:**

* GitHub repository: `holbertonschool-higher_level_programming`
* Directory: `0x12-javascript-warm_up`
* File: `1-multi_languages.js`

Each container will be available 24h max
```
martin@ubuntu:~/0x12$ ./1-multi_languages.js
C is fun
Python is cool
Javascript is amazing
martin@ubuntu:~/0x12$

```



*[top](#0x12-Javascript---Warm-up)*

---


### 2. Arguments
File: **[2-arguments.js](2-arguments.js)**

Write a script that prints a message depending of the number of arguments passed:

* If no arguments are passed to the script, print “No argument”
* If only one argument is passed to the script, print “Argument found”
* Otherwise, print “Arguments found”
* You must use `console.log(...)` to print all output
* You are not allowed to use `var`

Reference: [process.argv](/rltoken/E5x0rMmgii1g_Da9R7DUag)

**Repo:**

* GitHub repository: `holbertonschool-higher_level_programming`
* Directory: `0x12-javascript-warm_up`
* File: `2-arguments.js`

Each container will be available 24h max
```
martin@ubuntu:~/0x12$ ./2-arguments.js
No argument
martin@ubuntu:~/0x12$ ./2-arguments.js Holberton
Argument found
martin@ubuntu:~/0x12$ ./2-arguments.js Holberton School
Arguments found
martin@ubuntu:~/0x12$

```



*[top](#0x12-Javascript---Warm-up)*

---


### 3. Value of my argument
File: **[3-value_argument.js](3-value_argument.js)**

Write a script that prints the first argument passed to it:

* If no arguments are passed to the script, print “No argument”
* You must use `console.log(...)` to print all output
* You are not allowed to use `var`
* You are not allowed to use `length`

**Repo:**

* GitHub repository: `holbertonschool-higher_level_programming`
* Directory: `0x12-javascript-warm_up`
* File: `3-value_argument.js`

Each container will be available 24h max
```
martin@ubuntu:~/0x12$ ./3-value_argument.js
No argument
martin@ubuntu:~/0x12$ ./3-value_argument.js Holberton
Holberton
martin@ubuntu:~/0x12$

```



*[top](#0x12-Javascript---Warm-up)*

---


### 4. Create a sentence
File: **[4-concat.js](4-concat.js)**

Write a script that prints two arguments passed to it, in the following format: “ is ”

* You must use `console.log(...)` to print all output
* You are not allowed to use `var`

**Repo:**

* GitHub repository: `holbertonschool-higher_level_programming`
* Directory: `0x12-javascript-warm_up`
* File: `4-concat.js`

Each container will be available 24h max
```
martin@ubuntu:~/0x12$ ./4-concat.js c cool
c is cool
martin@ubuntu:~/0x12$ ./4-concat.js c
c is undefined
martin@ubuntu:~/0x12$ ./4-concat.js
undefined is undefined
martin@ubuntu:~/0x12$

```



*[top](#0x12-Javascript---Warm-up)*

---


### 5. An Integer
File: **[5-to_integer.js](5-to_integer.js)**

Write a script that prints `My number: &lt;first argument converted in integer&gt;` if the first argument can be converted to an integer:

* If the argument can’t be converted to an integer, print “Not a number”
* You must use `console.log(...)` to print all output
* You are not allowed to use `var`
* You are not allowed to use `try/catch`

**Repo:**

* GitHub repository: `holbertonschool-higher_level_programming`
* Directory: `0x12-javascript-warm_up`
* File: `5-to_integer.js`

Each container will be available 24h max
```
martin@ubuntu:~/0x12$ ./5-to_integer.js
Not a number
martin@ubuntu:~/0x12$ ./5-to_integer.js 89
My number: 89
martin@ubuntu:~/0x12$ ./5-to_integer.js "89"
My number: 89
martin@ubuntu:~/0x12$ ./5-to_integer.js 89.89
My number: 89
martin@ubuntu:~/0x12$ ./5-to_integer.js Holberton
Not a number
martin@ubuntu:~/0x12$

```



*[top](#0x12-Javascript---Warm-up)*

---


### 6. Loop to languages
File: **[6-multi_languages_loop.js](6-multi_languages_loop.js)**

Write a script that prints 3 lines: (like `1-multi_languages.js`) but by using an array of string and a loop

* The first line: “C is fun”
* The second line: “Python is cool”
* The third line: “Javascript is amazing”
* You must use `console.log(...)` to print all output
* You are not allowed to use `var`
* You are not allowed to use any `if/else` statement
* You can use only one `console.log`
* You must use a loop (`while`, `for`, etc.)

**Repo:**

* GitHub repository: `holbertonschool-higher_level_programming`
* Directory: `0x12-javascript-warm_up`
* File: `6-multi_languages_loop.js`

Each container will be available 24h max
```
martin@ubuntu:~/0x12$ ./6-multi_languages_loop.js
C is fun
Python is cool
Javascript is amazing
martin@ubuntu:~/0x12$

```



*[top](#0x12-Javascript---Warm-up)*

---


### 7. I love C
File: **[7-multi_c.js](7-multi_c.js)**

Write a script that prints `x` times “C is fun”

* Where `x` is the first argument of the script
* If the first argument can’t be converted to an integer, print “Missing number of occurrences”
* You must use `console.log(...)` to print all output
* You are not allowed to use `var`
* You can use only two `console.log`
* You must use a loop (`while`, `for`, etc.)

**Repo:**

* GitHub repository: `holbertonschool-higher_level_programming`
* Directory: `0x12-javascript-warm_up`
* File: `7-multi_c.js`

Each container will be available 24h max
```
martin@ubuntu:~/0x12$ ./7-multi_c.js 2
C is fun
C is fun
martin@ubuntu:~/0x12$ ./7-multi_c.js 5
C is fun
C is fun
C is fun
C is fun
C is fun
martin@ubuntu:~/0x12$ ./7-multi_c.js
Missing number of occurrences
martin@ubuntu:~/0x12$ ./7-multi_c.js -3
martin@ubuntu:~/0x12$

```



*[top](#0x12-Javascript---Warm-up)*

---


### 8. Square
File: **[8-square.js](8-square.js)**

Write a script that prints a square

* The first argument is the size of the square
* If the first argument can’t be converted to an integer, print “Missing size”
* You must use the character `X` to print the square
* You must use `console.log(...)` to print all output
* You are not allowed to use `var`
* You must use a loop (`while`, `for`, etc.)

**Repo:**

* GitHub repository: `holbertonschool-higher_level_programming`
* Directory: `0x12-javascript-warm_up`
* File: `8-square.js`

Each container will be available 24h max
```
martin@ubuntu:~/0x12$ ./8-square.js
Missing size
martin@ubuntu:~/0x12$ ./8-square.js Holberton
Missing size
martin@ubuntu:~/0x12$ ./8-square.js 2
XX
XX
martin@ubuntu:~/0x12$ ./8-square.js 6
XXXXXX
XXXXXX
XXXXXX
XXXXXX
XXXXXX
XXXXXX
martin@ubuntu:~/0x12$ ./8-square.js -3
martin@ubuntu:~/0x12$

```



*[top](#0x12-Javascript---Warm-up)*

---


### 9. Add
File: **[9-add.js](9-add.js)**

Write a script that prints the addition of 2 integers

* The first argument is the first integer
* The second argument is the second integer
* You have to define a function with this prototype: `function add(a, b)`
* You must use `console.log(...)` to print all output
* You are not allowed to use `var`

**Repo:**

* GitHub repository: `holbertonschool-higher_level_programming`
* Directory: `0x12-javascript-warm_up`
* File: `9-add.js`

Each container will be available 24h max
```
martin@ubuntu:~/0x12$ ./9-add.js
NaN
martin@ubuntu:~/0x12$ ./9-add.js 1
NaN
martin@ubuntu:~/0x12$ ./9-add.js 1 7
8
martin@ubuntu:~/0x12$ ./9-add.js 13 89
102
martin@ubuntu:~/0x12$

```



*[top](#0x12-Javascript---Warm-up)*

---


### 10. Factorial
File: **[10-factorial.js](10-factorial.js)**

Write a script that computes and prints a factorial

* The first argument is integer (argument can be cast as integer) used for computing the factorial
* Factorial of `NaN` is `1`
* You must do it recursively
* You must use a function
* You must use `console.log(...)` to print all output
* You are not allowed to use `var`

**Repo:**

* GitHub repository: `holbertonschool-higher_level_programming`
* Directory: `0x12-javascript-warm_up`
* File: `10-factorial.js`

Each container will be available 24h max
```
martin@ubuntu:~/0x12$ ./10-factorial.js
1
martin@ubuntu:~/0x12$ ./10-factorial.js 3
6
martin@ubuntu:~/0x12$ ./10-factorial.js 89
1.6507955160908452e+136
martin@ubuntu:~/0x12$ ./10-factorial.js 333
Infinity
martin@ubuntu:~/0x12$

```



*[top](#0x12-Javascript---Warm-up)*

---


### 11. Second biggest!
File: **[11-second_biggest.js](11-second_biggest.js)**


```
martin@ubuntu:~/0x12$ ./11-second_biggest.js
0
martin@ubuntu:~/0x12$ ./11-second_biggest.js 1
0
martin@ubuntu:~/0x12$ ./11-second_biggest.js 4 2 5 3 0 -3
4
martin@ubuntu:~/0x12$

```



*[top](#0x12-Javascript---Warm-up)*

---


### 12. Object
File: **[12-object.js](12-object.js)**

Update this script to replace the value `12` with `89`:

* You are not allowed to use `var`

**Repo:**

* GitHub repository: `holbertonschool-higher_level_programming`
* Directory: `0x12-javascript-warm_up`
* File: `12-object.js`

Each container will be available 24h max
```
martin@ubuntu:~/0x12$ cat 12-object.js
#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
/*
YOUR CODE HERE
*/
console.log(myObject);

martin@ubuntu:~/0x12$ ./12-object.js
{ type: 'object', value: 12 }
{ type: 'object', value: 89 }
martin@ubuntu:~/0x12$

```



*[top](#0x12-Javascript---Warm-up)*

---


### 13. Add file
File: **[13-add.js](13-add.js)**


```
martin@ubuntu:~/0x12$ cat 13-main.js
#!/usr/bin/node
const add = require('./13-add').add;
console.log(add(3, 5));
martin@ubuntu:~/0x12$ ./13-main.js
8
martin@ubuntu:~/0x12$

```



*[top](#0x12-Javascript---Warm-up)*

---



