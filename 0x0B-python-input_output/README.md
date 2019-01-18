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

* Prototype: `def read_file(filename=""):`
* You must use the `with` statement
* You don’t need to manage file permission/file doesn’t exist exceptions.
* You are not allowed to import any module


```
$ ./0-main.py
Holberton School offers a truly innovative approach to education:
focus on building reliable applications and scalable systems, take on real-world
challenges, collaborate with your peers. 

A school every software engineer would have dreamt of!
$ 
```

### [1-number_of_lines](1-number_of_lines.py)


* Prototype: `def read_lines(filename="", nb_lines=0):`
* Read the entire file if `nb_lines` is lower or equal to `0` OR greater or equal to the total number of lines of the file
* You must use the `with` statement
* You don’t need to manage file permission/file doesn’t exist exceptions.
* You are not allowed to import any module


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


* Prototype: `def read_lines(filename="", nb_lines=0):`
* Read the entire file if `nb_lines` is lower or equal to `0` OR greater or equal to the total number of lines of the file
* You must use the `with` statement
* You don’t need to manage file permission/file doesn’t exist exceptions.
* You are not allowed to import any module


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


* Prototype: `def write_file(filename="", text=""):`
* You must use the `with` statement
* You don’t need to manage file permission exceptions.
* Your function should create the file if doesn’t exist.
* Your function should overwrite the content of the file if it already exists.
* You are not allowed to import any module


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


* Prototype: `def append_write(filename="", text=""):`
* If the file doesn’t exist, it should be created
* You must use the `with` statement
* You don’t need to manage file permission/file doesn’t exist exceptions.
* You are not allowed to import any module


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

</details>

**Example**
```
$ ./6-main.py
[1, 2, 3]
<class 'list'>
{'id': 12, 'is_active': True, 'name': 'John', 'info': {'age': 36, 'average': 3.14}, 'places': ['San Francisco', 'Tokyo']}
<class 'dict'>
[ValueError] Expecting property name enclosed in double quotes: line 2 column 25 (char 25)
```

### [7-save_to_json_file](7-save_to_json_file.py)

function that writes an Object to a text file, using a JSON representation


* Prototype: `def save_to_json_file(my_obj, filename):`
* You must use the `with` statement
* You don’t need to manage exceptions if the object can’t be serialized.
* You don’t need to manage file permission exceptions.


<details>
<summary><b>Test main</b></summary>

```Python
#!/usr/bin/python3
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file

filename = "my_list.json"
my_list = [1, 2, 3]
save_to_json_file(my_list, filename)

filename = "my_dict.json"
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
save_to_json_file(my_dict, filename)

try:
    filename = "my_set.json"
    my_set = { 132, 3 }
    save_to_json_file(my_set, filename)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
```

</details>

**Example**
```
$ ./7-main.py
[TypeError] {3, 132} is not JSON serializable
$ cat my_list.json ; echo ""
[1, 2, 3]
$ cat my_dict.json ; echo ""
{"name": "John", "places": ["San Francisco", "Tokyo"], "id": 12, "info": {"average": 3.14, "age": 36}, "is_active": true}
$ cat my_set.json ; echo ""

$ 

```

### [8-load_from_json_file](8-load_from_json_file.py)

function that creates an Object from a “JSON file”:


* Prototype: `def load_from_json_file(filename):`
* You must use the `with` statement
* You don’t need to manage exceptions if the JSON string doesn’t represent an object.
* You don’t need to manage file permissions / exceptions.


**my_fake.json**
```
{"is_active": true, 12 }
```

<details>
<summary><b>Test Main</b></summary>

```Python
#!/usr/bin/python3
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

filename = "my_list.json"
my_list = load_from_json_file(filename)
print(my_list)
print(type(my_list))

filename = "my_dict.json"
my_dict = load_from_json_file(filename)
print(my_dict)
print(type(my_dict))

try:
    filename = "my_set_doesnt_exist.json"
    my_set = load_from_json_file(filename)
    print(my_set)
    print(type(my_set))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    filename = "my_fake.json"
    my_fake = load_from_json_file(filename)
    print(my_fake)
    print(type(my_fake))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
```

</details>

**Example**

```
$ cat my_list.json ; echo ""
[1, 2, 3]
$ cat my_dict.json ; echo ""
{"name": "John", "places": ["San Francisco", "Tokyo"], "id": 12, "info": {"average": 3.14, "age": 36}, "is_active": true}
$ cat my_fake.json ; echo ""
{"is_active": true, 12 }
$ ./8-main.py
[1, 2, 3]
<class 'list'>
{'name': 'John', 'info': {'age': 36, 'average': 3.14}, 'id': 12, 'places': ['San Francisco', 'Tokyo'], 'is_active': True}
<class 'dict'>
[FileNotFoundError] [Errno 2] No such file or directory: 'my_set_doesnt_exist.json'
[ValueError] Expecting property name enclosed in double quotes: line 1 column 21 (char 20)
```

### [9-add_item](9-add_item.py)

script that adds all arguments to a Python list, and then save them to a file


* You must use your function `save_to_json_file` from `7-save_to_json_file.py`
* You must use your function `load_from_json_file` from `8-load_from_json_file.py`
* The list must be saved as a JSON representation in a file named `add_item.json`
* If the file doesn’t exist, it should be created
* You don’t need to manage file permissions / exceptions.


```Python
```

### [10-class_to_json](10-class_to_json.py)

function that returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object:


* Prototype: `def class_to_json(obj):`
* `obj` is an instance of a Class
* All attributes of the `obj` Class are serializable: list, dictionary, string, integer and boolean
* You are not allowed to import any module


### [11-student](11-student.py)

class Student that defines a student by:


* Public instance attributes: 

* Instantiation with `first_name`, `last_name` and `age`: `def __init__(self, first_name, last_name, age):`
 * `first_name`
 * `last_name`
 * `age`
* Public method `def to_json(self):` that retrieves a dictionary representation of a `Student` instance (same as `10-class_to_json.py`)
* You are not allowed to import any module


```Python
#!/usr/bin/python3
Student = __import__('11-student').Student

students = [Student("John", "Doe", 23), Student("Bob", "Dylan", 27)]

for student in students:
    j_student = student.to_json()
    print(type(j_student))
    print(j_student['first_name'])
    print(type(j_student['first_name']))
    print(j_student['age'])
    print(type(j_student['age']))
```

**Example**

```
$ ./11-main.py 
<class 'dict'>
John
<class 'str'>
23
<class 'int'>
<class 'dict'>
Bob
<class 'str'>
27
<class 'int'>
$
```

### [12-student](12-student.py)

continue from 11-student.py

### [13-student](13-studnet.py)




