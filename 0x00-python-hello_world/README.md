# 0x00. Python - Hello, World

This is the first module of my Python projects. From this project i should learn the following.

* Why Python programming is awesome (don’t forget to tweet today, with the hashtag #pythoniscool :))
* Who created Python
* Who is Guido van Rossum
* Where does the name ‘Python’ come from
* What is the Zen of Python
* How to use the Python interpreter
* How to print text and variables using print
* How to use strings
* What are indexing and slicing in Python
* What is the official Holberton Python coding style and how to check your code with PEP 8

## Tasks


### [0-run](./0-run)

Write a Shell script that runs a Python script.
The Python file name will be saved in the environment variable `$PYFILE`

```
$ cat main.py
#!/usr/bin/python3
print("Holberton School")

$ export PYFILE=main.py
$ ./0-run
Holberton School
$
```
---
### [1-run_inline](./1-run_inline)


Write a Shell script that runs Python code.

The Python code will be saved in the environment variable `$PYCODE`



### [2-print](2-print.py)


Write a Python script that prints exactly "Programming is like building a multilingual puzzle, followed by a new line.
* Use the function `print`

```
$ ./2-print.py
"Programming is like building a multilingual puzzle
$
```
---

### [3-print_number](3-print_number.py)


Complete this [source](https://github.com/holbertonschool/0x00.py/blob/master/3-print_number.py) code in order to print the integer stored in the variable `number`, followed by `Battery street`, followed by a new line.

* The output of the script should be:
  * the number, followed by Battery street,
  * followed by a new line
* are not allowed to cast the variable number into a string
* code must be 3 lines long
* have to use the new print numbers tips

```
$ ./3-print_number.py
98 Battery street
$
```
---

### [4-print_float](4-print_float.py)


Complete the [source code](https://github.com/holbertonschool/0x00.py/blob/master/4-print_float.py) in order to print the float stored in the variable `number` with a precision of 2 digits.

* The output of the program should be:
  * Float:, followed by the float with only 2 digits
  * followed by a new line
* are not allowed to cast number to string
* have to use the new print formatting tips

---

### [5-print_string](5-print_string.py)


Complete this [`source code`](https://github.com/holbertonschool/0x00.py/blob/master/5-print_string.py) in order to print 3 times a string stored in the variable str, followed by its first 9 characters.

* The output of the program should be:
  * 3 times the value of str
  * followed by a new line
  * followed by the 9 first characters of str
  * followed by a new line
* You are not allowed to use any loops or conditional statement
* Your program should be maximum 5 lines long

```
$ ./5-print_string.py
Holberton SchoolHolberton SchoolHolberton School
Holberton
$
```

---

### [6-concat](6-concat.py)


Complete this [`source code`](https://github.com/holbertonschool/0x00.py/blob/master/6-concat.py) to print Welcome to Holberton School!

You are not allowed to use any loops or conditional statements.
You have to use the variables `str1` and `str2` in your new line of code
Your program should be exactly 5 lines long

```
$ ./6-concat.py
Welcome to Holberton School!
$ wc -l 6-concat.py
5 6-concat.py
$
```

---

### [7-edges](7-edges.py)


Complete this [`source code`](https://github.com/holbertonschool/0x00.py/blob/master/7-edges.py)


* are not allowed to use any loops or conditional statements
* program should be exactly 8 lines long
* `word_first_3` should contain the first 3 letters of the variable `word`
* `word_last_2` should contain the last 2 letters of the variable `word`
* `middle_word` should contain the value of the variable `word` without the first and last letters

```
$ ./7-edges.py
First 3 letters: Hol
Last 2 letters: on
Middle word: olberto
$ wc -l 7-edges.py
8 7-edges.py
$

```

---

### [8-concat_edges](8-concat_edges.py)


Complete this [`source code`](https://github.com/holbertonschool/0x00.py/blob/master/8-concat_edges.py) to print `object-oriented programming with Python`, followed by a new line.

* You are not allowed to use any loops or conditional statements
* Your program should be exactly 5 lines long
* You are not allowed to create new variables
* You are not allowed to use string literals

```
$ ./8-concat_edges.py
object-oriented programming with Python
$ wc -l 8-concat_edges.py
5 8-concat_edges.py
$
```

---

### [9-easter_egg](9-easter_egg.py)


Write a Python script that prints “The Zen of Python”, by TimPeters, followed by a new line.

* Your script should be maximum 98 characters long (please check with `wc -m 9-easter_egg.py`)

```
$ ./9-easter_egg.py
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
$
```

---

### [10-check_cycle](10-check_cycle.c) [lists.h](lists.h)
**Technical interview preparation:**

* You are not allowed to google anything
* Whiteboard first
* This task and all future technical interview prep tasks will include checks for the efficiency of your solution, i.e. is your solution’s runtime fast enough, does your solution require extra memory usage / mallocs, etc.


Write a function in C that checks if a singly linked list has a cycle in it.

* Prototype: `int check_cycle(listint_t *list);`
* Return: `0` if there is no cycle, `1` if there is a cycle

Requirements:
* Only these functions are allowed: `write`, `printf`, `putchar`, `puts`, `malloc`, `free`


<details>
<summary>Provided Source</summary>

**list.h**

```C
#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 * for Holberton project
 */
typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint(listint_t **head, const int n);
void free_listint(listint_t *head);
int check_cycle(listint_t *list);

#endif /* LISTS_H */

```

**10-linked_lists.c**

```C
#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * print_listint - prints all elements of a listint_t list
 * @h: pointer to head of list
 * Return: number of nodes
 */
size_t print_listint(const listint_t *h)
{
    const listint_t *current;
    unsigned int n; /* number of nodes */

    current = h;
    n = 0;
    while (current != NULL)
    {
        printf("%i\n", current->n);
        current = current->next;
        n++;
    }

    return (n);
}

/**
 * add_nodeint - adds a new node at the beginning of a listint_t list
 * @head: pointer to a pointer of the start of the list
 * @n: integer to be included in node
 * Return: address of the new element or NULL if it fails
 */
listint_t *add_nodeint(listint_t **head, const int n)
{
    listint_t *new;

    new = malloc(sizeof(listint_t));
    if (new == NULL)
        return (NULL);

    new->n = n;
    new->next = *head;
    *head = new;

    return (new);
}

/**
 * free_listint - frees a listint_t list
 * @head: pointer to list to be freed
 * Return: void
 */
void free_listint(listint_t *head)
{
    listint_t *current;

    while (head != NULL)
    {
        current = head;
        head = head->next;
        free(current);
    }
}
```

**10-main.c**

```C
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * main - check the code for Holberton School students.
 *
 * Return: Always 0.
 */
int main(void)
{
    listint_t *head;
    listint_t *current;
    listint_t *temp;
    int i;

    head = NULL;
    add_nodeint(&head, 0);
    add_nodeint(&head, 1);
    add_nodeint(&head, 2);
    add_nodeint(&head, 3);
    add_nodeint(&head, 4);
    add_nodeint(&head, 98);
    add_nodeint(&head, 402);
    add_nodeint(&head, 1024);
    print_listint(head);

    if (check_cycle(head) == 0)
        printf("Linked list has no cycle\n");
    else if (check_cycle(head) == 1)
        printf("Linked list has a cycle\n");

    current = head;
    for (i = 0; i < 4; i++)
        current = current->next;
    temp = current->next;
    current->next = head;

    if (check_cycle(head) == 0)
        printf("Linked list has no cycle\n");
    else if (check_cycle(head) == 1)
        printf("Linked list has a cycle\n");

    current = head;
    for (i = 0; i < 4; i++)
        current = current->next;
    current->next = temp;

    free_listint(head);

    return (0);
}
```

</details>


**Output**

```
$ gcc 10-main.c 10-check_cycle.c 10-linked_lists.c -o cycle
$ ./cycle
1024
402
98
4
3
2
1
0
Linked list has no cycle
Linked list has a cycle
$
```


