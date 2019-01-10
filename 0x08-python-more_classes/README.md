# 0x08. Python - More Classes and Objects

<li>What is OOP</li>
<li>“first-class everything”</li>
<li>What is a class</li>
<li>What is an object and an instance</li>
<li>What is the difference between a class and an object or instance</li>
<li>What is an attribute</li>
<li>What are and how to use public, protected and private attributes</li>
<li>What is <code>self</code></li>
<li>What is a method</li>
<li>What is the special <code>__init__</code> method and how to use it</li>
<li>What is Data Abstraction, Data Encapsulation, and Information Hiding</li>
<li>What is a property</li>
<li>What is the difference between an attribute and a property in Python</li>
<li>What is the Pythonic way to write getters and setters in Python</li>
<li>What are the special <code>__str__</code> and <code>__repr__</code> methods and how to use them</li>
<li>What is the difference between <code>__str__</code> and <code>__repr__</code></li>
<li>What is a class attribute</li>
<li>What is the difference between a object attribute and a class attribute</li>
<li>What is a class method</li>
<li>What is a static method</li>
<li>How to dynamically create arbitrary new attributes for existing instances of a class</li>
<li>How to bind attributes to object and classes</li>
<li>What is and what does contain <code>__dict__</code> of a class and of an instance of a class</li>
<li>How does Python find the attributes of an object or class</li>
<li>How to use the <code>getattr</code> function</li>

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

building on top of  class <code>Rectangle</code> that defines a rectangle 

<li>Private instance attribute: <code>width</code>:

<ul>
<li>property <code>def width(self):</code> to retrieve it</li>
<li>property setter <code>def width(self, value):</code> to set it:

<ul>
<li><code>width</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>width must be an integer</code><br></li>
<li>if <code>width</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>width must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<li>Private instance attribute: <code>height</code>:

<ul>
<li>property <code>def height(self):</code> to retrieve it</li>
<li>property setter <code>def height(self, value):</code> to set it:

<ul>
<li><code>height</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>height must be an integer</code><br></li>
<li>if <code>height</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>height must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<li>Instantiation with optional <code>width</code> and <code>height</code>: <code>def __init__(self, width=0, height=0):</code></li>
<li>You are not allowed to import any module</li>


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

building on top of  class <code>Rectangle</code> that defines a rectangle 

**Title:  Area and Perimeter**

building on top of  class <code>Rectangle</code> from previous task.

<li>Private instance attribute: <code>width</code>:

<ul>
<li>property <code>def width(self):</code> to retrieve it</li>
<li>property setter <code>def width(self, value):</code> to set it:

<ul>
<li><code>width</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>width must be an integer</code><br></li>
<li>if <code>width</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>width must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<li>Private instance attribute: <code>height</code>:

<ul>
<li>property <code>def height(self):</code> to retrieve it</li>
<li>property setter <code>def height(self, value):</code> to set it:

<ul>
<li><code>height</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>height must be an integer</code><br></li>
<li>if <code>height</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>height must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<li>Instantiation with optional <code>width</code> and <code>height</code>: <code>def __init__(self, width=0, height=0):</code></li>
<li>Public instance method: <code>def area(self):</code> that returns the rectangle area</li>
<li>Public instance method: <code>def perimeter(self):</code> that returns the rectangle perimeter:

<ul>
<li>if <code>width</code> or <code>height</code> is equal to <code>0</code>, perimeter is equal to <code>0</code></li>
</ul></li>
<li>You are not allowed to import any module</li>


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

building on top of  class <code>Rectangle</code> that defines a rectangle 

<li>Private instance attribute: <code>width</code>:

<ul>
<li>property <code>def width(self):</code> to retrieve it</li>
<li>property setter <code>def width(self, value):</code> to set it:

<ul>
<li><code>width</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>width must be an integer</code><br></li>
<li>if <code>width</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>width must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<li>Private instance attribute: <code>height</code>:

<ul>
<li>property <code>def height(self):</code> to retrieve it</li>
<li>property setter <code>def height(self, value):</code> to set it:

<ul>
<li><code>height</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>height must be an integer</code><br></li>
<li>if <code>height</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>height must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<li>Instantiation with optional <code>width</code> and <code>height</code>: <code>def __init__(self, width=0, height=0):</code></li>
<li>Public instance method: <code>def area(self):</code> that returns the rectangle area</li>
<li>Public instance method: <code>def perimeter(self):</code> that returns the rectangle perimeter:

<ul>
<li>if <code>width</code> or <code>height</code> is equal to <code>0</code>, perimeter has to be equal to <code>0</code></li>
</ul></li>
<li><code>print()</code> and <code>str()</code> should print the rectangle with the character <code>#</code>: (see example below)

<ul>
<li>if <code>width</code> or <code>height</code> is equal to 0, return an empty string</li>
</ul></li>
<li>You are not allowed to import any module</li>


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

<details>

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

building on top of  class <code>Rectangle</code> that defines a rectangle 

- <code>repr()</code> should return a string representation of the rectangle to be able to recreate a new instance by using <code>eval()</code> (see example below)

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

building on top of  class <code>Rectangle</code> that defines a rectangle 

- Print the message <code>Bye rectangle...</code> (<code>...</code> being 3 dots not ellipsis) when an instance of <code>Rectangle</code> is deleted

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

building on top of  class <code>Rectangle</code> that defines a rectangle 

- Public class attribute <code>number_of_instances</code>:
<ul>
<li>Initialized to <code>0</code></li>
<li>Incremented during each new instance instantiation</li>
<li>Decremented during each instance deletion</li>
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

building on top of  class <code>Rectangle</code> that defines a rectangle 

- Public class attribute <code>print_symbol</code>:
<li>Initialized to <code>#</code></li>
<li>Used as symbol for string representation</li>
<li>Can be any type</li>
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

building on top of  class <code>Rectangle</code> that defines a rectangle 

Static method <code>def bigger_or_equal(rect_1, rect_2):</code> that returns the biggest rectangle based on the area

<ul>
<li><code>rect_1</code> must be an instance of <code>Rectangle</code>, otherwise raise a <code>TypeError</code> exception with the message <code>rect_1 must be an instance of Rectangle</code><br></li>
<li><code>rect_2</code> must be an instance of <code>Rectangle</code>, otherwise raise a <code>TypeError</code> exception with the message <code>rect_2 must be an instance of Rectangle</code><br></li>
<li>Returns <code>rect_1</code> if both have the same area value</li>
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

building on top of  class <code>Rectangle</code> that defines a rectangle 

- Class method <code>def square(cls, size=0):</code> that returns a new Rectangle instance with <code>width == height == size</code>

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

