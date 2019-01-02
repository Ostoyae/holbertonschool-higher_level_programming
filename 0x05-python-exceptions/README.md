# 0x05. Python - Exceptions
## Details
This project we learn about exceptions through it we should learn the following.

- What’s the difference between errors and exceptions
- What are exceptions and how to use them
- When do we need to use exceptions
- How to correctly handle an exception
- What’s the purpose of catching exceptions
- How to raise a builtin exception
- When do we need to implement a clean-up action after an exception

## Tasks

### [0-safe_print_list](http://./0-safe_print_list.py)
Function that prints the `x`elements in a list

- Prototype: `def safe_print_list(my_list=[], x=0):`
- `my_list` can contain any type (integer, string, etc.)
- All elements must be printed on the same line followed by a new line.
- `x` represents the number of elements to print
- `x` can be bigger than the length of `my_list`
- Returns the real number of elements printed
- You have to use `try: / except:` 
- You are not allowed to import any module
- You are not allowed to use `len()`

<details>
<summary> Test file: 0-main.py</summary>

```python
#!/usr/bin/python3                                                    
safe_print_list = __import__('0-safe_print_list').safe_print_list     
                                                                      
my_list = [1, 2, 3, 4, 5]                                             
                                                                      
nb_print = safe_print_list(my_list, 2)                                
print("nb_print: {:d}".format(nb_print))                              
nb_print = safe_print_list(my_list, len(my_list))                     
print("nb_print: {:d}".format(nb_print))                              
nb_print = safe_print_list(my_list, len(my_list) + 2)                 
print("nb_print: {:d}".format(nb_print))                              
                                                                      
my_list = []                                                          
nb_print = safe_print_list(my_list, 2)                                
print("nb_print: {:d}".format(nb_print))                              
```


</details>

```markdown
$ ./0-main.py
12
nb_print: 2
12345
nb_print: 5
12345
nb_print: 5


nb_print: 0
```


---

### [1-safe_print_integer](http://./1-safe_print_integer.py)

This Function prints an interger with `"{:d}".format()`


- Prototype: `def safe_print_integer(value):`
- `value` can be any type (integer, string, etc.)
- The integer should be printed followed by a new line
- Returns `True` if `value` has been correctly printed (it means the `value` is an integer)
- Otherwise, returns `False`
- You have to use `try: / except:` 
- You have to use `"{:d}".format()` to print as integer
- You are not allowed to import any module
- You are not allowed to use `type()`

<details>
<summary>Test file: 1-main.py</summary>

```python
#!/usr/bin/python3
safe_print_integer = __import__('1-safe_print_integer').safe_print_integer

value = 89
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = -89
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = "Holberton"
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))
```

</details>

**Example**

```markdown
$ ./1-main.py
89
-89
Holberton is not an integer

```

---

### [2-safe_print_list_integers](http://./2-safe_print_list_integers.py)

Write a function that prints the first x elements of a list and only integers.

- Prototype: `def safe_print_list_integers(my_list=[], x=0):`
- `my_list` can contain any type (integer, string, etc.)
- All integers have to be printed on the same line followed by a new line.
- `x` represents the number of elements to access in `my_list`
- `x` can be bigger than the length of `my_list`
- Returns the real number of integers printed
- You have to use `try: / except:` 
- You have to use `"{:d}".format()` to print an integer
- You are not allowed to import any module
- You are not allowed to use `len()`



<details>
<summary>**Test file: 2-main.py**</summary>

```python
#!/usr/bin/python3
safe_print_list_integers = \
    __import__('2-safe_print_list_integers').safe_print_list_integers

my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list_integers(my_list, 2)
print("nb_print: {:d}".format(nb_print))

my_list = [1, 2, 3, "Holberton", 4, 5, [1, 2, 3]]
nb_print = safe_print_list_integers(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))

nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))
```

</details>

**Example**

```markdown
$ ./2-main.py
12
nb_print: 2
12345
nb_print: 5
12345Traceback (most recent call last):
  File "./2-main.py", line 14, in <module>
    nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
  File "/0x05/2-safe_print_list_integers.py", line 7, in safe_print_list_integers
    print("{:d}".format(my_list[i]), end="")
IndexError: list index out of range
```

---

### [3-safe_print_division](http://./3-safe_print_division.py)

Write a function that divides 2 integers and prints the result.

- Prototype: `def safe_print_division(a, b):`
- You can assume that `a` and `b` are integers
- The result of the division should print on the `finally:` section preceded by `Inside result:`
- Returns the value of the division, otherwise: `None`
- You have to use `try: / except: / finally:` 
- You have to use `"{}".format()` to print the result
- You are not allowed to import any module

<details>
<summary>**Test file: 3-main.py**</summary>

```python
#!/usr/bin/python3
safe_print_division = __import__('3-safe_print_division').safe_print_division

a = 12
b = 2
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))

a = 12
b = 0
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))
```

</details>

**Example**

```markdown
$ ./3-main.py
Inside result: 6.0
12 / 2 = 6.0
Inside result: None
12 / 0 = None
```

---

### [4-list_division](http://./4-list_division.py)
Write a function that divides element by element 2 lists.

- Prototype: `def list_division(my_list_1, my_list_2, list_length):`
- `my_list_1` and `my_list_2` can contain any type (integer, string, etc.)
- `list_length` can be bigger than the length of both lists
- Returns a new list (length = `list_length`) with all divisions
- If 2 elements can’t be divided, the division result should be equal to `0`
- If an element is not an integer or float:
  - print: `wrong type`

- If the division can’t be done (`/0`):
  - print: `division by 0`

- If `my_list_1` or `my_list_2` is too short
  - print: `out of range`

- You have to use `try: / except: / finally:` 
- You are not allowed to import any module

<details>
<summary>**Test file: 4-main.py**</summary>

```python
#!/usr/bin/python3
list_division = __import__('4-list_division').list_division

my_l_1 = [10, 8, 4]
my_l_2 = [2, 4, 4]
result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
print(result)

print("--")

my_l_1 = [10, 8, 4, 4]
my_l_2 = [2, 0, "H", 2, 7]
result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
print(result)
```

</details>

**Example**

```markdown
$ ./4-main.py
[5.0, 2.0, 1.0]
--
division by 0
wrong type
out of range
[5.0, 0, 0, 2.0, 0]
```

---

### [5-raise_exception](http://./5-raise_exception.py)
function that raises a type exception.
- Prototype: `def raise_exception():`
- You are not allowed to import any module

**Test file: 5-main.py**
```python
#!/usr/bin/python3
raise_exception = __import__('5-raise_exception').raise_exception

try:
    raise_exception()
except TypeError as te:
    print("Exception raised")

```

**Example**

```markdown
$ ./5-main.py
Exception raised
```

---

### [6-raise_exception_msg](http://6-raise_exception_msg.py)
function that raises a name exception with a message.
- Prototype: `def raise_exception_msg(message=""):`
- You are not allowed to import any module

**Test file: 6-main.py**
```python
#!/usr/bin/python3
raise_exception_msg = __import__('6-raise_exception_msg').raise_exception_msg

try:
    raise_exception_msg("C is fun")
except NameError as ne:
    print(ne)
```

**Example**

```markdown
$ ./6-main.py
C is fun
$
```



