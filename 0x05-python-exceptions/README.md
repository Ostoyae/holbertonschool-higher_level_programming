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

### []()
### []()
### []()
### []()
### []()
### []()
