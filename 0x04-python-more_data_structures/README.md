# 0x04. Python - More Data Structures: Set, Dictionary

## Tasks

### [0-square_matrix_simple](./0-square_matrix_simple.py)

Write a function that computes the square value of all integers of a matrix.


* Prototype: `def square_matrix_simple(matrix=[]):`
* `matrix` is a 2 dimensional array
* Returns a new matrix:

	* Same size as `matrix`
	* Each value should be the square of the value of the input
* Initial matrix should not be modified
* You are not allowed to import any module
* You are allowed to use regular loops, `map`, etc.

```Python

#!/usr/bin/python3
square_matrix_simple = __import__('0-square_matrix_simple').square_matrix_simple

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(matrix)

```

```
$ ./0-main.py
[[1, 4, 9], [16, 25, 36], [49, 64, 81]]
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
$
```

---

### [1-search_replace](./1-search_replace.py)

Write a function that replaces all occurrences of an element by another in a new list.

* Prototype: `def search_replace(my_list, search, replace):`
* `my_list` is the initial list
* `search` is the element to replace in the list
* `replace` is the new element
* You are not allowed to import any module

```Python
#!/usr/bin/python3
search_replace = __import__('1-search_replace').search_replace

my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
new_list = search_replace(my_list, 2, 89)

print(new_list)
print(my_list)
```

**Demo**
```
$ ./1-main.py
[1, 89, 3, 4, 5, 4, 89, 1, 1, 4, 89]
[1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
```

---

### [2-uniq_add](./2-uniq_add.py)

Write a function that adds all unique integers in a list (only once for each integer).


* Prototype: `def uniq_add(my_list=[]):`
* You are not allowed to import any module

**Test file**
```Python
#!/usr/bin/python3
uniq_add = __import__('2-uniq_add').uniq_add

my_list = [1, 2, 3, 1, 4, 2, 5]
result = uniq_add(my_list)
print("Result: {:d}".format(result))
```

**Demo**
```
$ ./2-main.py
Result: 15
$
```

---

### [3-common_elements](./3-common_elements.py)

Write a function that returns a set of common elements in two sets


* Prototype: `def common_elements(set_1, set_2):`
* You are not allowed to import any module

**Test File**

```Python
#!/usr/bin/python3
common_elements = __import__('3-common_elements').common_elements

set_1 = { "Python", "C", "Javascript" }
set_2 = { "Bash", "C", "Ruby", "Perl" }
c_set = common_elements(set_1, set_2)
print(sorted(list(c_set)))

```

**Demo**

```
$ ./3-main.py
['C']
$
```

---

### [4-only_diff_elements](./4-only_diff_elements.py)

Write a function that returns a set of all elements present in only one set.


* Prototype: `def only_diff_elements(set_1, set_2):`
* You are not allowed to import any module

**Test file**

```Python
#!/usr/bin/python3
only_diff_elements = __import__('4-only_diff_elements').only_diff_elements

set_1 = { "Python", "C", "Javascript" }
set_2 = { "Bash", "C", "Ruby", "Perl" }
od_set = only_diff_elements(set_1, set_2)
print(sorted(list(od_set)))
```

**Demo**

```
$ ./4-main.py
['Bash', 'Javascript', 'Perl', 'Python', 'Ruby']
$
```

---

### [5-number_keys](./5-number_keys.py)

Write a function that returns the number of keys in a dictionary.


* Prototype: `def number_keys(a_dictionary):`
* You are not allowed to import any module

**Test File**

```Python
#!/usr/bin/python3
number_keys = __import__('5-number_keys').number_keys

a_dictionary = { 'language': "C", 'number': 13, 'track': "Low level" }
nb_keys = number_keys(a_dictionary)
print("Number of keys: {:d}".format(nb_keys))
```

**Demo**

```
$ ./5-main.py
Number of keys: 3
$
```

---

### [6-print_sorted_dictionary](./6-print_sorted_dictionary.py)

Write a function that prints a dictionary by ordered keys.


* Prototype: `def print_sorted_dictionary(a_dictionary):`
* You can assume that all keys are strings
* Keys should be sorted by alphabetic order
* Only sort keys of the first level (don’t sort keys of a dictionary inside the main dictionary)
* Dictionary values can have any type
* You are not allowed to import any module


### [7-update_dictionary](./7-update_dictionary.py)

Write a function that replaces or adds key/value in a dictionary.


* Prototype: `def update_dictionary(a_dictionary, key, value):`
* `key` argument will be always a string
* `value` argument will be any type
* If a key exists in the dictionary, the value will be replaced
* If a key doesn’t exist in the dictionary, it will be created
* You are not allowed to import any module

<details>
<summary>**Test File</summary>

```Python

#!/usr/bin/python3
update_dictionary = __import__('7-update_dictionary').update_dictionary
print_sorted_dictionary = __import__('6-print_sorted_dictionary').print_sorted_dictionary

a_dictionary = { 'language': "C", 'number': 89, 'track': "Low level" }
new_dict = update_dictionary(a_dictionary, 'language', "Python")
print_sorted_dictionary(new_dict)
print("--")
print_sorted_dictionary(a_dictionary)

print("--")
print("--")

new_dict = update_dictionary(a_dictionary, 'city', "San Francisco")
print_sorted_dictionary(new_dict)
print("--")
print_sorted_dictionary(a_dictionary)

```

</details>

**Demo**

```
$ ./7-main.py
language: Python
number: 89
track: Low level
--
language: Python
number: 89
track: Low level
--
--
city: San Francisco
language: Python
number: 89
track: Low level
--
city: San Francisco
language: Python
number: 89
track: Low level
```

---


