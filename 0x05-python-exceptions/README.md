# 0x05. Python - Exceptions

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

---

### [3-safe_print_division](http://./3-safe_print_division.py)

---

### [4-list_division](http://./4-list_division.py)

---

### [5-raise_exception](http://./5-raise_exception.py)

---

### [6-raise_exception_msg](http://6-raise_exception_msg.py)
