# 0x11. Python - Network #1


**Table Of Context**
- [0. What's my status? #0](#0-What's-my-status?-0)
- [1. Response header value #0](#1-Response-header-value-0)
- [2. POST an email #0](#2-POST-an-email-0)
- [3. Error code #0](#3-Error-code-0)
- [4. What's my status? #1](#4-What's-my-status?-1)
- [5. Response header value #1](#5-Response-header-value-1)
- [6. POST an email #1](#6-POST-an-email-1)
- [7. Error code #1](#7-Error-code-1)
- [8. Search API](#8-Search-API)
- [9. Star Wars API #0](#9-Star-Wars-API-0)
- [10. My Github!](#10-My-Github!)


## Tasks


### 0. What's my status? #0
File: **[0-hbtn_status.py](0-hbtn_status.py)**




```
martin@ubuntu:~/0x11$ ./0-hbtn_status.py | cat -e
Body response:$
    - type: <class 'bytes'>$
    - content: b'OK'$
    - utf8 content: OK$
martin@ubuntu:~/0x11$

```



*[top](#0x11-Python---Network-1)*

---


### 1. Response header value #0
File: **[1-hbtn_header.py](1-hbtn_header.py)**




```
martin@ubuntu:~/0x11$ ./1-hbtn_header.py https://intranet.hbtn.io
ade2627e-41dd-4c34-b9d9-a0fa0f47b237
martin@ubuntu:~/0x11$
martin@ubuntu:~/0x11$ ./1-hbtn_header.py https://intranet.hbtn.io
6593e1f5-1b4b-4c9f-9c0e-72ab525b850f
martin@ubuntu:~/0x11$

```



*[top](#0x11-Python---Network-1)*

---


### 2. POST an email #0
File: **[2-post_email.py](2-post_email.py)**

Write a Python script that takes in a URL and an email, sends a `POST` request to the passed URL with the email as a parameter, and displays the body of the response (decoded in `utf-8`)

* The email must be sent in the `email` variable
* You must use the packages `urllib` and `sys`
* You are not allowed to import packages other than `urllib` and `sys`
* You don’t need to check arguments passed to the script (number or type)
* You must use the `with` statement

Please test your script in the container provided, using the web server running on port 5000

**Repo:**

* GitHub repository: `holbertonschool-higher_level_programming`
* Directory: `0x11-python-network_1`
* File: `2-post_email.py`

Each container will be available 24h max


```
martin@ubuntu:~/0x11$ ./2-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com
Your email is: hr@holbertonschool.com
martin@ubuntu:~/0x11$

```



*[top](#0x11-Python---Network-1)*

---


### 3. Error code #0
File: **[3-error_code.py](3-error_code.py)**

Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response (decoded in `utf-8`).

* You have to manage `urllib.error.HTTPError` exceptions and print: `Error code:` followed by the HTTP status code
* You must use the packages `urllib` and `sys`
* You are not allowed to import other packages than `urllib` and `sys`
* You don’t need to check arguments passed to the script (number or type)
* You must use the `with` statement

Please test your script in the container provided, using the web server running on port 5000

**Repo:**

* GitHub repository: `holbertonschool-higher_level_programming`
* Directory: `0x11-python-network_1`
* File: `3-error_code.py`

Each container will be available 24h max


```
martin@ubuntu:~/0x11$ ./3-error_code.py http://0.0.0.0:5000
Index
martin@ubuntu:~/0x11$ ./3-error_code.py http://0.0.0.0:5000/status_401
Error code: 401
martin@ubuntu:~/0x11$ ./3-error_code.py http://0.0.0.0:5000/doesnt_exist
Error code: 404
martin@ubuntu:~/0x11$ ./3-error_code.py http://0.0.0.0:5000/status_500
Error code: 500
martin@ubuntu:~/0x11$

```



*[top](#0x11-Python---Network-1)*

---


### 4. What's my status? #1
File: **[4-hbtn_status.py](4-hbtn_status.py)**




```
martin@ubuntu:~/0x11$ ./4-hbtn_status.py | cat -e
Body response:$
    - type: <class 'str'>$
    - content: OK$
martin@ubuntu:~/0x11$

```



*[top](#0x11-Python---Network-1)*

---


### 5. Response header value #1
File: **[5-hbtn_header.py](5-hbtn_header.py)**




```
martin@ubuntu:~/0x11$ ./5-hbtn_header.py https://intranet.hbtn.io
5e52e160-c822-4669-8b3a-8b3bbca7b090
martin@ubuntu:~/0x11$
martin@ubuntu:~/0x11$ ./5-hbtn_header.py https://intranet.hbtn.io
eaceaf35-bc0f-4f74-994a-7be0728ec654
martin@ubuntu:~/0x11$

```



*[top](#0x11-Python---Network-1)*

---


### 6. POST an email #1
File: **[6-post_email.py](6-post_email.py)**

Write a Python script that takes in a URL and an email address, sends a `POST` request to the passed URL with the email as a parameter, and finally displays the body of the response.

* The email must be sent in the variable `email`
* You must use the packages `requests` and `sys`
* You are not allowed to import packages other than `requests` and `sys`
* You don’t need to error check arguments passed to the script (number or type)

Please test your script in the container provided, using the web server running on port 5000

**Repo:**

* GitHub repository: `holbertonschool-higher_level_programming`
* Directory: `0x11-python-network_1`
* File: `6-post_email.py`

Each container will be available 24h max


```
martin@ubuntu:~/0x11$ ./6-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com
Your email is: hr@holbertonschool.com
martin@ubuntu:~/0x11$

```



*[top](#0x11-Python---Network-1)*

---


### 7. Error code #1
File: **[7-error_code.py](7-error_code.py)**

Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response.

* If the HTTP status code is greater than or equal to 400, print: `Error code:` followed by the value of the HTTP status code
* You must use the packages `requests` and `sys`
* You are not allowed to import packages other than `requests` and `sys`
* You don’t need to check arguments passed to the script (number or type)

Please test your script in the container provided, using the web server running on port 5000

**Repo:**

* GitHub repository: `holbertonschool-higher_level_programming`
* Directory: `0x11-python-network_1`
* File: `7-error_code.py`

Each container will be available 24h max


```
martin@ubuntu:~/0x11$ ./7-error_code.py http://0.0.0.0:5000
Index
martin@ubuntu:~/0x11$ ./7-error_code.py http://0.0.0.0:5000/status_401
Error code: 401
martin@ubuntu:~/0x11$ ./7-error_code.py http://0.0.0.0:5000/doesnt_exist
Error code: 404
martin@ubuntu:~/0x11$ ./7-error_code.py http://0.0.0.0:5000/status_500
Error code: 500
martin@ubuntu:~/0x11$

```



*[top](#0x11-Python---Network-1)*

---


### 8. Search API
File: **[8-json_api.py](8-json_api.py)**

Write a Python script that takes in a letter and sends a `POST` request to `http://0.0.0.0:5000/search_user` with the letter as a parameter.

* The letter must be sent in the variable `q`
* If no argument is given, set `q=&quot;&quot;`
* If the response body is properly JSON formatted and not empty, display the `id` and `name` like this: `[&lt;id&gt;] &lt;name&gt;`
* Otherwise:
  * Display `Not a valid JSON` is the JSON is invalid
  * Display `No result` is the JSON is empty

* You must use the package `requests` and `sys`
* You are not allowed to import packages other than `requests` and `sys`

* Display `Not a valid JSON` is the JSON is invalid
* Display `No result` is the JSON is empty

Please test your script in the container provided, using the web server running on port 5000. All JSON generated by this server are random.

**Repo:**

* GitHub repository: `holbertonschool-higher_level_programming`
* Directory: `0x11-python-network_1`
* File: `8-json_api.py`

Each container will be available 24h max


```
martin@ubuntu:~/0x11$ ./8-json_api.py
No result
martin@ubuntu:~/0x11$ ./8-json_api.py a
[8446] amnirqhtfjq
martin@ubuntu:~/0x11$ ./8-json_api.py 2
No result
martin@ubuntu:~/0x11$ ./8-json_api.py b
[7094] bmofakakhke
martin@ubuntu:~/0x11$

```



*[top](#0x11-Python---Network-1)*

---


### 9. Star Wars API #0
File: **[9-starwars.py](9-starwars.py)**




```
martin@ubuntu:~/0x11$ ./9-starwars.py r2
Number of results: 1
R2-D2
martin@ubuntu:~/0x11$ ./9-starwars.py lu
Number of results: 2
Luke Skywalker
Luminara Unduli
martin@ubuntu:~/0x11$ ./9-starwars.py ju
Number of results: 0
martin@ubuntu:~/0x11$ ./9-starwars.py g
Number of results: 16
Leia Organa
Biggs Darklighter
Greedo
Wedge Antilles
IG-88
Qui-Gon Jinn
Nute Gunray
Rugor Nass
Gasgano
Adi Gallia
martin@ubuntu:~/0x11$

```



*[top](#0x11-Python---Network-1)*

---


### 10. My Github!
File: **[10-my_github.py](10-my_github.py)**




```
martin@ubuntu:~/0x11$ ./10-my_github.py papamuziko cisfun
2531536
martin@ubuntu:~/0x11$ ./10-my_github.py papamuziko wrong_pwd
None
martin@ubuntu:~/0x11$

```



*[top](#0x11-Python---Network-1)*

---




