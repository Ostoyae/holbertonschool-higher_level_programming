# 0x08. Python - More Classes and Objects


<details>
<summary><b>Details</b></summary>

* What is OOP
* "first-class everything"
* What is a class
* What is an object and an instance
* What is the difference between a class and an object or instance
* What is an attribute
* What are and how to use public, protected and private attributes
* What is `self`
* What is a method
* What is the special `__init__` method and how to use it
* What is Data Abstraction, Data Encapsulation, and Information Hiding
* What is a property
* What is the difference between an attribute and a property in Python
* What is the Pythonic way to write getters and setters in Python
* What are the special `__str__` and `__repr__` methods and how to use them
* What is the difference between `__str__` and `__repr__`
* What is a class attribute
* What is the difference between a object attribute and a class attribute
* What is a class method
* What is a static method
* How to dynamically create arbitrary new attributes for existing instances of a class
* How to bind attributes to object and classes
* What is and what does contain `__dict__` of a class and of an instance of a class
* How does Python find the attributes of an object or class
* How to use the `getattr` function

</details>

## TASKS

### [0-rectangle](0-rectangle.py)

**Title: Simple rectangle**

<b>Test</b>

```python
#!/usr/bin/python3
Rectangle = __import__('0-rectangle').Rectangle

my_rectangle = Rectangle()
print(type(my_rectangle))
print(my_rectangle.__dict__)
```

**Example**

```markdown
$ ./0-main.py
<class '0-rectangle.Rectangle'>
{}
$
```


---

### [1-rectangle](1-rectangle.py)

**Title:**  **Real definition of a rectangle**

building on top of  class `Rectangle` that defines a rectangle

* Private instance attribute: `width`:

<ul>
* property `def width(self):` to retrieve it
* property setter `def width(self, value):` to set it:

<ul>
* `width` must be an integer, otherwise raise a `TypeError` exception with the message `width must be an integer`<br>
* if `width` is less than `0`, raise a `ValueError` exception with the message `width must be &gt;= 0`
</ul>
</ul>
* Private instance attribute: `height`:

<ul>
* property `def height(self):` to retrieve it
* property setter `def height(self, value):` to set it:

<ul>
* `height` must be an integer, otherwise raise a `TypeError` exception with the message `height must be an integer`<br>
* if `height` is less than `0`, raise a `ValueError` exception with the message `height must be &gt;= 0`
</ul>
</ul>
* Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
* You are not allowed to import any module


<b>Test File:  1-main.py</b>
```python
#!/usr/bin/python3
Rectangle = __import__('1-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print(my_rectangle.__dict__)

my_rectangle.width = 10
my_rectangle.height = 3
print(my_rectangle.__dict__)
```


**Example**

```markdown
$ ./1-main.py
{'_Rectangle__height': 4, '_Rectangle__width': 2}
{'_Rectangle__height': 3, '_Rectangle__width': 10}
$
```


---

### [2-rectangle](2-rectangle.py)

building on top of  class `Rectangle` that defines a rectangle

**Title:  Area and Perimeter**

building on top of  class `Rectangle` from previous task.

* Private instance attribute: `width`:

<ul>
* property `def width(self):` to retrieve it
* property setter `def width(self, value):` to set it:

<ul>
* `width` must be an integer, otherwise raise a `TypeError` exception with the message `width must be an integer`<br>
* if `width` is less than `0`, raise a `ValueError` exception with the message `width must be &gt;= 0`
</ul>
</ul>
* Private instance attribute: `height`:

<ul>
* property `def height(self):` to retrieve it
* property setter `def height(self, value):` to set it:

<ul>
* `height` must be an integer, otherwise raise a `TypeError` exception with the message `height must be an integer`<br>
* if `height` is less than `0`, raise a `ValueError` exception with the message `height must be &gt;= 0`
</ul>
</ul>
* Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
* Public instance method: `def area(self):` that returns the rectangle area
* Public instance method: `def perimeter(self):` that returns the rectangle perimeter:

<ul>
* if `width` or `height` is equal to `0`, perimeter is equal to `0`
</ul>
* You are not allowed to import any module


<details>
<summary><b>Test File: 2-main.py</b></summary>

```python
#!/usr/bin/python3
Rectangle = __import__('2-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

print("--")

my_rectangle.width = 10
my_rectangle.height = 3
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))
```

</details>

**Example**

```markdown
$ ./2-main.py
Area: 8 - Perimeter: 12
--
Area: 30 - Perimeter: 26
$
```


---

### [3-rectangle](3-rectangle.py)

building on top of  class `Rectangle` that defines a rectangle

* Private instance attribute: `width`:

<ul>
* property `def width(self):` to retrieve it
* property setter `def width(self, value):` to set it:

<ul>
* `width` must be an integer, otherwise raise a `TypeError` exception with the message `width must be an integer`<br>
* if `width` is less than `0`, raise a `ValueError` exception with the message `width must be &gt;= 0`
</ul>
</ul>
* Private instance attribute: `height`:

<ul>
* property `def height(self):` to retrieve it
* property setter `def height(self, value):` to set it:

<ul>
* `height` must be an integer, otherwise raise a `TypeError` exception with the message `height must be an integer`<br>
* if `height` is less than `0`, raise a `ValueError` exception with the message `height must be &gt;= 0`
</ul>
</ul>
* Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
* Public instance method: `def area(self):` that returns the rectangle area
* Public instance method: `def perimeter(self):` that returns the rectangle perimeter:

<ul>
* if `width` or `height` is equal to `0`, perimeter has to be equal to `0`
</ul>
* `print()` and `str()` should print the rectangle with the character `#`: (see example below)

<ul>
* if `width` or `height` is equal to 0, return an empty string
</ul>
* You are not allowed to import any module


**Test File: 3-main.py**

```python
#!/usr/bin/python3
Rectangle = __import__('3-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

print(str(my_rectangle))
print(repr(my_rectangle))

print("--")

my_rectangle.width = 10
my_rectangle.height = 3
print(my_rectangle)
print(repr(my_rectangle))
```

**Example**

```markdown
$ ./3-main.py
Area: 8 - Perimeter: 12
##
##
##
##
<3-rectangle.Rectangle object at 0x7f92a75a2eb8>
--
##########
##########
##########
<3-rectangle.Rectangle object at 0x7f92a75a2eb8>
$
```


---

### [4-rectangle](4-rectangle.py)

building on top of  class `Rectangle` that defines a rectangle

- `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()` (see example below)

<details>
<summary><b>Test File: 4-main.py</b></summary>

```python
#!/usr/bin/python3
Rectangle = __import__('4-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print(str(my_rectangle))
print("--")
print(my_rectangle)
print("--")
print(repr(my_rectangle))
print("--")
print(hex(id(my_rectangle)))
print("--")

# create new instance based on representation
new_rectangle = eval(repr(my_rectangle))
print(str(new_rectangle))
print("--")
print(new_rectangle)
print("--")
print(repr(new_rectangle))
print("--")
print(hex(id(new_rectangle)))
print("--")

print(new_rectangle is my_rectangle)
print(type(new_rectangle) is type(my_rectangle))
```

<details>

<details>
<summary><b>Example</b></summary>

```markdown
$ ./4-main.py
##
##
##
##
--
##
##
##
##
--
Rectangle(2, 4)
--
0x7f09ebf7cc88
--
##
##
##
##
--
##
##
##
##
--
Rectangle(2, 4)
--
0x7f09ebf7ccc0
--
False
True
$
```

</details>

---

### [5-rectangle](5-rectangle.py)

building on top of  class `Rectangle` that defines a rectangle

- Print the message `Bye rectangle...` (`...` being 3 dots not ellipsis) when an instance of `Rectangle` is deleted

<details>
<summary><b>Test File: 5-main.py</b></summary>

```python
#!/usr/bin/python3
Rectangle = __import__('5-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

del my_rectangle

try:
    print(my_rectangle)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
```

<details>

**Example**

```markdown
$ ./5-main.py
Area: 8 - Perimeter: 12
Bye rectangle...
[NameError] name 'my_rectangle' is not defined
$
```


---


### [6-rectangle](6-rectangle.py)

building on top of  class `Rectangle` that defines a rectangle

- Public class attribute `number_of_instances`:
<ul>
* Initialized to `0`
* Incremented during each new instance instantiation
* Decremented during each instance deletion
</ul>

<details>
<summary><b>Test File: 6-main.py</b></summary>

```python
#!/usr/bin/python3
Rectangle = __import__('6-rectangle').Rectangle

my_rectangle_1 = Rectangle(2, 4)
my_rectangle_2 = Rectangle(2, 4)
print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))
del my_rectangle_1
print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))
del my_rectangle_2
print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))
```

<details>

**Example**

```markdown
$ ./6-main.py
2 instances of Rectangle
Bye rectangle...
1 instances of Rectangle
Bye rectangle...
0 instances of Rectangle
$
```


---


### [7-rectangle](7-rectangle.py)

building on top of  class `Rectangle` that defines a rectangle

- Public class attribute `print_symbol`:
* Initialized to `#`
* Used as symbol for string representation
* Can be any type
</ul>


<details>
<summary><b>Test File: 7-main.py</b></summary>

```python
#!/usr/bin/python3
Rectangle = __import__('7-rectangle').Rectangle

my_rectangle_1 = Rectangle(8, 4)
print(my_rectangle_1)
print("--")
my_rectangle_1.print_symbol = "&"
print(my_rectangle_1)
print("--")

my_rectangle_2 = Rectangle(2, 1)
print(my_rectangle_2)
print("--")
Rectangle.print_symbol = "C"
print(my_rectangle_2)
print("--")

my_rectangle_3 = Rectangle(7, 3)
print(my_rectangle_3)

print("--")

my_rectangle_3.print_symbol = ["C", "is", "fun!"]
print(my_rectangle_3)

print("--")

```

<details>

<details>
<summary><b>Example</b></summary>

```markdown
$ ./7-main.py
########
########
########
########
--
&&&&&&&&
&&&&&&&&
&&&&&&&&
&&&&&&&&
--
##
--
CC
--
CCCCCCC
CCCCCCC
CCCCCCC
--
['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']
['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']
['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']
--
Bye rectangle...
Bye rectangle...
Bye rectangle...
$
```

</details>

---


### [8-rectangle](8-rectangle.py)

building on top of  class `Rectangle` that defines a rectangle

Static method `def bigger_or_equal(rect_1, rect_2):` that returns the biggest rectangle based on the area

<ul>
* `rect_1` must be an instance of `Rectangle`, otherwise raise a `TypeError` exception with the message `rect_1 must be an instance of Rectangle`<br>
* `rect_2` must be an instance of `Rectangle`, otherwise raise a `TypeError` exception with the message `rect_2 must be an instance of Rectangle`<br>
* Returns `rect_1` if both have the same area value
</ul>

<details>
<summary><b>Test File: 8-main.py</b></summary>

```python
#!/usr/bin/python3
Rectangle = __import__('8-rectangle').Rectangle

my_rectangle_1 = Rectangle(8, 4)
my_rectangle_2 = Rectangle(2, 3)

if Rectangle.bigger_or_equal(my_rectangle_1, my_rectangle_2):
    print("my_rectangle_1 is bigger or equal to my_rectangle_2")
else:
    print("my_rectangle_2 is bigger than my_rectangle_1")


my_rectangle_2.width = 10
my_rectangle_2.height = 5
if my_rectangle_1 is Rectangle.bigger_or_equal(my_rectangle_1, my_rectangle_2):
    print("my_rectangle_1 is bigger or equal to my_rectangle_2")
else:
    print("my_rectangle_2 is bigger than my_rectangle_1")
```

<details>

**Example**

```markdown
$ ./8-main.py
my_rectangle_1 is bigger or equal to my_rectangle_2
my_rectangle_2 is bigger than my_rectangle_1
Bye rectangle...
Bye rectangle...
$
```


---


### [9-rectangle](9-rectangle.py)

building on top of  class `Rectangle` that defines a rectangle

- Class method `def square(cls, size=0):` that returns a new Rectangle instance with `width == height == size`

**Test File: 9-main.py**

```python
#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle

my_square = Rectangle.square(5)
print("Area: {} - Perimeter: {}".format(my_square.area(), my_square.perimeter()))
print(my_square)
```


**Example**

```markdown
$ ./9-main.py
Area: 25 - Perimeter: 20
#####
#####
#####
#####
#####
Bye rectangle...
$
```


---

