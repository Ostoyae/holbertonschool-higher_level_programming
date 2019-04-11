# 0x10. Python - Network #0


**Table Of Context**
- [0. cURL body size](#0-cURL-body-size)
- [1. cURL to the end](#1-cURL-to-the-end)
- [2. cURL Method](#2-cURL-Method)
- [3. cURL only methods](#3-cURL-only-methods)
- [4. cURL headers](#4-cURL-headers)
- [5. cURL POST parameters](#5-cURL-POST-parameters)
- [6. Find a peak](#6-Find-a-peak)


## Tasks


### 0. cURL body size
File: **[0-body_size.sh](0-body_size.sh)**

Write a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response

* The size must be displayed in bytes
* You have to use `curl`

Please test your script in the container provided, using the web server running on port 5000


```
martin@ubuntu:~/0x10$ ./0-body_size.sh 0.0.0.0:5000
10
martin@ubuntu:~/0x10$

```



*[top](#0x10-Python---Network-#0)*

---


### 1. cURL to the end
File: **[1-body.sh](1-body.sh)**

Write a Bash script that takes in a URL, sends a `GET` request to the URL, and displays the body of the response

* Display only body of a `200` status code response
* You have to use `curl`

Please test your script in the container provided, using the web server running on port 5000


```
martin@ubuntu:~/0x10$ ./1-body.sh 0.0.0.0:5000/route_1 ; echo ""
Route 2
martin@ubuntu:~/0x10$

```



*[top](#0x10-Python---Network-#0)*

---


### 2. cURL Method
File: **[2-delete.sh](2-delete.sh)**

Write a Bash script that sends a `DELETE` request to the URL passed as the first argument and displays the body of the response

* You have to use `curl`

Please test your script in the container provided, using the web server running on port 5000


```
martin@ubuntu:~/0x10$ ./2-delete.sh 0.0.0.0:5000/route_3 ; echo ""
I'm a DELETE request
martin@ubuntu:~/0x10$

```



*[top](#0x10-Python---Network-#0)*

---


### 3. cURL only methods
File: **[3-methods.sh](3-methods.sh)**

Write a Bash script that takes in a URL and displays all HTTP methods the server will accept.

* You have to use `curl`

Please test your script in the container provided, using the web server running on port 5000


```
martin@ubuntu:~/0x10$ ./3-methods.sh 0.0.0.0:5000/route_4
OPTIONS, HEAD, PUT
martin@ubuntu:~/0x10$

```



*[top](#0x10-Python---Network-#0)*

---


### 4. cURL headers
File: **[4-header.sh](4-header.sh)**

Write a Bash script that takes in a URL as an argument, sends a `GET` request to the URL, and displays the body of the response

* A header variable `X-HolbertonSchool-User-Id` must be sent with the value `98`
* You have to use `curl`

Please test your script in the container provided, using the web server running on port 5000


```
martin@ubuntu:~/0x10$ ./4-header.sh 0.0.0.0:5000/route_5 ; echo ""
Hello Holberton School!
martin@ubuntu:~/0x10$

```



*[top](#0x10-Python---Network-#0)*

---


### 5. cURL POST parameters
File: **[5-post_params.sh](5-post_params.sh)**

Write a Bash script that takes in a URL, sends a `POST` request to the passed URL, and displays the body of the response

* A variable `email` must be sent with the value `hr@holbertonschool.com`
* A variable `subject` must be sent with the value `I will always be here for PLD`
* You have to use `curl`

Please test your script in the container provided, using the web server running on port 5000



```
guillaume@ubuntu:~/0x10$ ./5-post_params.sh 0.0.0.0:5000/route_6 ; echo ""
POST params:
martin@holbertonschool.com
    subject: I will always be here for PLD
guillaume@ubuntu:~/0x10$

```



*[top](#0x10-Python---Network-#0)*

---


### 6. Find a peak
File: **[6-peak.py, 6-peak.txt](6-peak.py, 6-peak.txt)**




```
martin@ubuntu:~/0x10$ cat 6-main.py
#!/usr/bin/python3
""" Test function find_peak """
find_peak = __import__('6-peak').find_peak

print(find_peak([1, 2, 4, 6, 3]))
print(find_peak([4, 2, 1, 2, 3, 1]))
print(find_peak([2, 2, 2]))
print(find_peak([]))
print(find_peak([-2, -4, 2, 1]))
print(find_peak([4, 2, 1, 2, 3, 1]))

martin@ubuntu:~/0x10$ ./6-main.py
6
3
2
None
2
4
martin@ubuntu:~/0x10$ wc -l 6-peak.txt
2 6-peak.txt
martin@ubuntu:~/0x10$

```



*[top](#0x10-Python---Network-#0)*

---

