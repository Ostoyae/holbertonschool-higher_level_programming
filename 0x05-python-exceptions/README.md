# 0x05. Python - Exceptions

## Tasks

### [0-safe_print_list](./0-safe_print_list.py)
Function that prints the `x`elements in a list

<li>Prototype: <code>def safe_print_list(my_list=[], x=0):</code></li>
<li><code>my_list</code> can contain any type (integer, string, etc.)</li>
<li>All elements must be printed on the same line followed by a new line.</li>
<li><code>x</code> represents the number of elements to print</li>
<li><code>x</code> can be bigger than the length of <code>my_list</code></li>
<li>Returns the real number of elements printed</li>
<li>You have to use <code>try: / except:</code> </li>
<li>You are not allowed to import any module</li>
<li>You are not allowed to use <code>len()</code></li>

<details>
<summary> Test file: 0-main.py</summary>

```Python
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

```
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

### [1-safe_print_integer](./1-safe_print_integer.py)

This Function prints an interger with `"{:d}".format()`


<li>Prototype: <code>def safe_print_integer(value):</code></li>
<li><code>value</code> can be any type (integer, string, etc.)</li>
<li>The integer should be printed followed by a new line</li>
<li>Returns <code>True</code> if <code>value</code> has been correctly printed (it means the <code>value</code> is an integer)</li>
<li>Otherwise, returns <code>False</code></li>
<li>You have to use <code>try: / except:</code> </li>
<li>You have to use <code>"{:d}".format()</code> to print as integer</li>
<li>You are not allowed to import any module</li>
<li>You are not allowed to use <code>type()</code></li>

<details>
<summary>Test file: 1-main.py</summary>

```Python
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
```
$ ./1-main.py
89
-89
Holberton is not an integer
```

---

### [2-safe_print_list_integers](./2-safe_print_list_integers.py)

---

### [3-safe_print_division](./3-safe_print_division.py)

---

### [4-list_division](./4-list_division.py)

---

### [5-raise_exception](./5-raise_exception.py)

---

### [6-raise_exception_msg](6-raise_exception_msg.py)
