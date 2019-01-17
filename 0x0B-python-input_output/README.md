# 0x0B. Python - Input/Output

In this project I'll learn the following.

* How to open a file
* How to write text in a file
* How to read the full content of a file
* How to read a file line by line
* How to move the cursor in a file
* How to make sure a file is closed after using it
* What is and how to use the `with` statement
* What is `JSON`
* What is serialization
* What is deserialization
* How to convert a Python data structure to a `JSON` string
* How to convert a JSON string to a Python data structure

## Tasks

### [0-read_file](0-read_file.py)

function that reads a text file `(UTF8)` and prints it to stdout:
<ul>
<li>Prototype: <code>def read_file(filename=""):</code></li>
<li>You must use the <code>with</code> statement</li>
<li>You don’t need to manage file permission/file doesn’t exist exceptions.</li>
<li>You are not allowed to import any module</li>
</ul>

```
$ ./0-main.py
Holberton School offers a truly innovative approach to education:
focus on building reliable applications and scalable systems, take on real-world
challenges, collaborate with your peers. 

A school every software engineer would have dreamt of!
$ 
```

### [1-number_of_lines](1-number_of_lines.py)

<ul>
<li>Prototype: <code>def read_lines(filename="", nb_lines=0):</code></li>
<li>Read the entire file if <code>nb_lines</code> is lower or equal to <code>0</code> OR greater or equal to the total number of lines of the file</li>
<li>You must use the <code>with</code> statement</li>
<li>You don’t need to manage file permission/file doesn’t exist exceptions.</li>
<li>You are not allowed to import any module</li>
</ul>

```Python
#!/usr/bin/python3
number_of_lines = __import__('1-number_of_lines').number_of_lines

filename = "my_file_0.txt"
nb_lines = number_of_lines(filename)
print("{} has {:d} lines".format(filename, nb_lines))
```

**Example**
```
$ wc -l my_file_0.txt
4 my_file_0.txt
$ ./1-main.py
my_file_0.txt has 4 lines
$ 
```

### [2-read_lines](2-read_lines.py)

function that reads `n` lines of a text file `(UTF8)` and prints it to stdout:

<ul>
<li>Prototype: <code>def read_lines(filename="", nb_lines=0):</code></li>
<li>Read the entire file if <code>nb_lines</code> is lower or equal to <code>0</code> OR greater or equal to the total number of lines of the file</li>
<li>You must use the <code>with</code> statement</li>
<li>You don’t need to manage file permission/file doesn’t exist exceptions.</li>
<li>You are not allowed to import any module</li>
</ul>

```Python
#!/usr/bin/python3
read_lines = __import__('2-read_lines').read_lines

print("1 line:")
read_lines("my_file_0.txt", 1)
print("--")
print("3 lines:")
read_lines("my_file_0.txt", 3)
print("--")
print("Full content:")
read_lines("my_file_0.txt")
```

**Example**
```
$ ./2-main.py
1 line:
Holberton School offers a truly innovative approach to education:
--
3 lines:
Holberton School offers a truly innovative approach to education:
focus on building reliable applications and scalable systems, take on real-world challenges, collaborate with your peers. 

--
Full content:
Holberton School offers a truly innovative approach to education:
focus on building reliable applications and scalable systems, take on real-world challenges, collaborate with your peers. 

A school every software engineer would have dreamt of!
$
```

### [3-write_file](3-write_file.py)

function that writes a string to a text file (UTF8) and returns the number of characters written:

<ul>
<li>Prototype: <code>def write_file(filename="", text=""):</code></li>
<li>You must use the <code>with</code> statement</li>
<li>You don’t need to manage file permission exceptions.</li>
<li>Your function should create the file if doesn’t exist.</li>
<li>Your function should overwrite the content of the file if it already exists.</li>
<li>You are not allowed to import any module</li>
</ul>

```Python
#!/usr/bin/python3
write_file = __import__('3-write_file').write_file

nb_characters = write_file("my_first_file.txt", "Holberton School is so cool!\n")
print(nb_characters)
```

**Eample**
```
$ ./3-main.py
29
$ cat my_first_file.txt
Holberton School is so cool!
$
```

### [4-append_write](4-append_write.py)

function that appends a string at the end of a text file (UTF8) and returns the number of characters added:

<ul>
<li>Prototype: <code>def append_write(filename="", text=""):</code></li>
<li>If the file doesn’t exist, it should be created</li>
<li>You must use the <code>with</code> statement</li>
<li>You don’t need to manage file permission/file doesn’t exist exceptions.</li>
<li>You are not allowed to import any module</li>
</ul>

```Python
#!/usr/bin/python3
append_write = __import__('4-append_write').append_write

nb_characters_added = append_write("file_append.txt", "Holberton School is so cool!\n")
print(nb_characters_added)
```

**Example**
```
$ cat file_append.txt
cat: file_append.txt: No such file or directory
$ ./4-main.py
29
$ cat file_append.txt
Holberton School is so cool!
$ ./4-main.py
29
$ cat file_append.txt
Holberton School is so cool!
Holberton School is so cool!
$
```

### [5-to_json_string](5-to_json_string.py)

function that returns the JSON representation of an object (string):

* Prototype: `def to_json_string(my_obj):`
* You don’t need to manage exceptions if the object can’t be serialized 

<details>
<summary><b>Test Main</b></summary>

```Python
#!/usr/bin/python3
to_json_string = __import__('5-to_json_string').to_json_string

my_list = [1, 2, 3]
s_my_list = to_json_string(my_list)
print(s_my_list)
print(type(s_my_list))

my_dict = { 
    'id': 12,
    'name': "John",
    'places': [ "San Francisco", "Tokyo" ],
    'is_active': True,
    'info': {
        'age': 36,
        'average': 3.14
    }
}
s_my_dict = to_json_string(my_dict)
print(s_my_dict)
print(type(s_my_dict))

try:
    my_set = { 132, 3 }
    s_my_set = to_json_string(my_set)
    print(s_my_set)
    print(type(s_my_set))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
```

</details>

**Example**
```
$ ./5-main.py
[1, 2, 3]
<class 'str'>
{"id": 12, "is_active": true, "name": "John", "info": {"average": 3.14, "age": 36}, "places": ["San Francisco", "Tokyo"]}
<class 'str'>
[TypeError] {3, 132} is not JSON serializable
$
```

### [6-from_json_string](6-from_json_string.py)

function that returns an object (Python data structure) represented by a JSON string:

* Prototype: `def from_json_string(my_str):`
* You don’t need to manage exceptions if the JSON string doesn’t represent an object.


<details>
<summary><b>Test Main</b></summary>

```Python
#!/usr/bin/python3
from_json_string = __import__('6-from_json_string').from_json_string

s_my_list = "[1, 2, 3]"
my_list = from_json_string(s_my_list)
print(my_list)
print(type(my_list))

s_my_dict = """
{"is_active": true, "info": {"age": 36, "average": 3.14}, 
"id": 12, "name": "John", "places": ["San Francisco", "Tokyo"]}
"""
my_dict = from_json_string(s_my_dict)
print(my_dict)
print(type(my_dict))

try:
    s_my_dict = """
    {"is_active": true, 12 }
    """
    my_dict = from_json_string(s_my_dict)
    print(my_dict)
    print(type(my_dict))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
```

**Example**
```
$ ./6-main.py
[1, 2, 3]
<class 'list'>
{'id': 12, 'is_active': True, 'name': 'John', 'info': {'age': 36, 'average': 3.14}, 'places': ['San Francisco', 'Tokyo']}
<class 'dict'>
[ValueError] Expecting property name enclosed in double quotes: line 2 column 25 (char 25)
```

</details>
