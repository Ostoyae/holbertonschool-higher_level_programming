# 0x0D. SQL - Introduction

## Tasks

### [0. List databases]

Write a script that lists all databases of your MySQL server.

**Repo:**

* GitHub repository: `holbertonschool-higher_level_programming`
* Directory: `0x0D-SQL_introduction`
* File: `0-list_databases.sql`

Each container will be available 24h max


```
martin@ubuntu:~/$cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
Enter password:
Database
information_schema
mysql
performance_schema
martin@ubuntu:~/$

```


---


### [1. Create a database](1-create_database_if_missing.sql)

Write a script that creates the database `hbtn_0c_0` in your MySQL server.

* If the database `hbtn_0c_0` already exists, your script should not fail
* You are not allowed to use the `SELECT` or `SHOW` statements

**Repo:**

* GitHub repository: `holbertonschool-higher_level_programming`
* Directory: `0x0D-SQL_introduction`
* File: `1-create_database_if_missing.sql`

Each container will be available 24h max


```
martin@ubuntu:~/$cat 1-create_database_if_missing.sql | mysql -hlocalhost -uroot -p
Enter password:
martin@ubuntu:~/$cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
Enter password:
Database
information_schema
hbtn_0c_0
mysql
performance_schema
martin@ubuntu:~/$cat 1-create_database_if_missing.sql | mysql -hlocalhost -uroot -p
Enter password:
martin@ubuntu:~/$

```


---


### [2. Delete a database](2-remove_database.sql)

Write a script that deletes the database `hbtn_0c_0` in your MySQL server.

* If the database `hbtn_0c_0` doesn’t exist, your script should not fail
* You are not allowed to use the `SELECT` or `SHOW` statements

**Repo:**

* GitHub repository: `holbertonschool-higher_level_programming`
* Directory: `0x0D-SQL_introduction`
* File: `2-remove_database.sql`

Each container will be available 24h max


```
martin@ubuntu:~/$cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
Enter password:
Database
information_schema
hbtn_0c_0
mysql
performance_schema
martin@ubuntu:~/$cat 2-remove_database.sql | mysql -hlocalhost -uroot -p
Enter password:
martin@ubuntu:~/$cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
Enter password:
Database
information_schema
mysql
performance_schema
martin@ubuntu:~/$

```


---


### [3. List tables](3-list_tables.sql)

Write a script that lists all the tables of a database in your MySQL server.

* The database name will be passed as argument of `mysql` command (in the following example: `mysql` is the name of the database)

**Repo:**

* GitHub repository: `holbertonschool-higher_level_programming`
* Directory: `0x0D-SQL_introduction`
* File: `3-list_tables.sql`

Each container will be available 24h max


```
martin@ubuntu:~/$cat 3-list_tables.sql | mysql -hlocalhost -uroot -p mysql
Enter password:
Tables_in_mysql
columns_priv
db
event
func
general_log
help_category
help_keyword
help_relation
help_topic
host
ndb_binlog_index
plugin
proc
procs_priv
proxies_priv
servers
slow_log
tables_priv
time_zone
time_zone_leap_second
time_zone_name
time_zone_transition
time_zone_transition_type
user
martin@ubuntu:~/$

```


---


### [4. First table](4-first_table.sql)

Write a script that creates a table called `first_table` in the current database in your MySQL server.

* `first_table` description:
  * `id` INT
  * `name` VARCHAR(256)

* The database name will be passed as an argument of the `mysql` command
* If the table `first_table` already exists, your script should not fail
* You are not allowed to use the `SELECT` or `SHOW` statements

* `id` INT
* `name` VARCHAR(256)

**Repo:**

* GitHub repository: `holbertonschool-higher_level_programming`
* Directory: `0x0D-SQL_introduction`
* File: `4-first_table.sql`

Each container will be available 24h max


```
martin@ubuntu:~/$cat 4-first_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password:
martin@ubuntu:~/$cat 3-list_tables.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password:
Tables_in_hbtn_0c_0
first_table
martin@ubuntu:~/$

```


---


### [5. Full description](5-full_table.sql)

Write a script that prints the full description of the table `first_table` from the database `hbtn_0c_0` in your MySQL server.

* The database name will be passed as an argument of the `mysql` command
* You are not allowed to use the `DESCRIBE` or `EXPLAIN` statements

**Repo:**

* GitHub repository: `holbertonschool-higher_level_programming`
* Directory: `0x0D-SQL_introduction`
* File: `5-full_table.sql`

Each container will be available 24h max


```
martin@ubuntu:~/$cat 5-full_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password:
Table   Create Table
first_table CREATE TABLE `first_table` (\n  `id` int(11) DEFAULT NULL,\n  `name` varchar(256) DEFAULT NULL\n) ENGINE=InnoDB DEFAULT CHARSET=latin1
martin@ubuntu:~/$

```


---


### [6. List all in table](6-list_values.sql)

Write a script that lists all rows of the table `first_table` from the database `hbtn_0c_0` in your MySQL server.

* All fields should be printed
* The database name will be passed as an argument of the `mysql` command

**Repo:**

* GitHub repository: `holbertonschool-higher_level_programming`
* Directory: `0x0D-SQL_introduction`
* File: `6-list_values.sql`

Each container will be available 24h max


```
martin@ubuntu:~/$cat 6-list_values.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password:
martin@ubuntu:~/$

```


---


### [7. First add](7-insert_value.sql)

Write a script that inserts a new row in the table `first_table` (database `hbtn_0c_0`) in your MySQL server.

* New row:
  * `id` = `89`
  * `name` = `Holberton School`

* The database name will be passed as an argument of the `mysql` command

* `id` = `89`
* `name` = `Holberton School`

**Repo:**

* GitHub repository: `holbertonschool-higher_level_programming`
* Directory: `0x0D-SQL_introduction`
* File: `7-insert_value.sql`

Each container will be available 24h max


```
martin@ubuntu:~/$cat 7-insert_value.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password:
martin@ubuntu:~/$cat 6-list_values.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password:
id  name
89  Holberton School
martin@ubuntu:~/$cat 7-insert_value.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password:
martin@ubuntu:~/$cat 7-insert_value.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password:
martin@ubuntu:~/$cat 6-list_values.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password:
id  name
89  Holberton School
89  Holberton School
89  Holberton School
martin@ubuntu:~/$

```


---


### [8. Count 89](8-count_89.sql)

Write a script that displays the number of records with `id = 89` in the table `first_table` of the database `hbtn_0c_0` in your MySQL server.

* The database name will be passed as an argument of the `mysql` command

**Repo:**

* GitHub repository: `holbertonschool-higher_level_programming`
* Directory: `0x0D-SQL_introduction`
* File: `8-count_89.sql`

Each container will be available 24h max


```
martin@ubuntu:~/$cat 8-count_89.sql | mysql -hlocalhost -uroot -p hbtn_0c_0 | tail -1
Enter password:
3
martin@ubuntu:~/$

```


---


### [9. Full creation](9-full_creation.sql)

Write a script that creates a table `second_table` in the database `hbtn_0c_0` in your MySQL server and add multiples rows.

* `second_table` description:
  * `id` INT
  * `name` VARCHAR(256)
  * `score` INT

* The database name will be passed as an argument to the `mysql` command
* If the table `second_table` already exists, your script should not fail
* You are not allowed to use the `SELECT` and `SHOW` statements
* Your script should create these records:
  * `id` = 1, `name` = “John”, `score` = 10
  * `id` = 2, `name` = “Alex”, `score` = 3
  * `id` = 3, `name` = “Bob”, `score` = 14
  * `id` = 4, `name` = “George”, `score` = 8

* `id` INT
* `name` VARCHAR(256)
* `score` INT

* `id` = 1, `name` = “John”, `score` = 10
* `id` = 2, `name` = “Alex”, `score` = 3
* `id` = 3, `name` = “Bob”, `score` = 14
* `id` = 4, `name` = “George”, `score` = 8

**Repo:**

* GitHub repository: `holbertonschool-higher_level_programming`
* Directory: `0x0D-SQL_introduction`
* File: `9-full_creation.sql`

Each container will be available 24h max


```
martin@ubuntu:~/$cat 9-full_creation.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password:
martin@ubuntu:~/$

```


---


### [10. List by best](10-top_score.sql)

Write a script that lists all records of the table `second_table` of the database `hbtn_0c_0` in your MySQL server.

* Results should display both the score and the name (in this order)
* Records should be ordered by score (top first)
* The database name will be passed as an argument of the `mysql` command

**Repo:**

* GitHub repository: `holbertonschool-higher_level_programming`
* Directory: `0x0D-SQL_introduction`
* File: `10-top_score.sql`

Each container will be available 24h max


```
martin@ubuntu:~/$cat 10-top_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password:
score   name
14  Bob
10  John
8   George
3   Alex
martin@ubuntu:~/$

```


---


### [11. Select the best](11-best_score.sql)

Write a script that lists all records with a `score &gt;= 10` in the table `second_table` of the database `hbtn_0c_0` in your MySQL server.

* Results should display both the score and the name (in this order)
* Records should be ordered by score (top first)
* The database name will be passed as an argument of the `mysql` command

**Repo:**

* GitHub repository: `holbertonschool-higher_level_programming`
* Directory: `0x0D-SQL_introduction`
* File: `11-best_score.sql`

Each container will be available 24h max


```
martin@ubuntu:~/$cat 11-best_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password:
score   name
14  Bob
10  John
martin@ubuntu:~/$

```


---


### [12. Cheating is bad](12-no_cheating.sql)

Write a script that updates the score of Bob to `10` in the table `second_table`.

* You are not allowed to use Bob’s id value, only the `name` field
* The database name will be passed as an argument of the `mysql` command

**Repo:**

* GitHub repository: `holbertonschool-higher_level_programming`
* Directory: `0x0D-SQL_introduction`
* File: `12-no_cheating.sql`

Each container will be available 24h max


```
martin@ubuntu:~/$cat 12-no_cheating.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password:
martin@ubuntu:~/$cat 10-top_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password:
score   name
10  John
10  Bob
8   George
3   Alex
martin@ubuntu:~/$

```


---


### [13. Score too low](13-change_class.sql)

Write a script that removes all records with a `score &lt;= 5` in the table `second_table` of the database `hbtn_0c_0` in your MySQL server.

* The database name will be passed as an argument of the `mysql` command

**Repo:**

* GitHub repository: `holbertonschool-higher_level_programming`
* Directory: `0x0D-SQL_introduction`
* File: `13-change_class.sql`

Each container will be available 24h max


```
martin@ubuntu:~/$cat 13-change_class.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password:
martin@ubuntu:~/$cat 10-top_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password:
score   name
10  John
10  Bob
8   George
martin@ubuntu:~/$

```


---


### [14. Average](14-average.sql)

Write a script that computes the score average of all records in the table `second_table` of the database `hbtn_0c_0` in your MySQL server.

* The result column name should be `average`
* The database name will be passed as an argument of the `mysql` command

**Repo:**

* GitHub repository: `holbertonschool-higher_level_programming`
* Directory: `0x0D-SQL_introduction`
* File: `14-average.sql`

Each container will be available 24h max


```
martin@ubuntu:~/$cat 14-average.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password:
average
9.3333
martin@ubuntu:~/$

```


---


### [15. Number by score](15-groups.sql)

Write a script that lists the number of records with the same score in the table `second_table` of the database `hbtn_0c_0` in your MySQL server.

* The result should display:
  * the `score`
  * the number of records for this `score` with the label `number`

* The list should be sorted by the number of records (descending)
* The database name will be passed as an argument to the `mysql` command

* the `score`
* the number of records for this `score` with the label `number`

**Repo:**

* GitHub repository: `holbertonschool-higher_level_programming`
* Directory: `0x0D-SQL_introduction`
* File: `15-groups.sql`

Each container will be available 24h max


```
martin@ubuntu:~/$cat 15-groups.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password:
score   number
10  2
8   1
martin@ubuntu:~/$

```


---


### [16. Say my name](16-no_link.sql)

Write a script that lists all records of the table `second_table` of the database `hbtn_0c_0` in your MySQL server.

* Don’t list rows without a `name` value
* Results should display the score and the name (in this order)
* Records should be listed by descending score
* The database name will be passed as an argument to the `mysql` command

In this example, new data have been added to the table `second_table`.

**Repo:**

* GitHub repository: `holbertonschool-higher_level_programming`
* Directory: `0x0D-SQL_introduction`
* File: `16-no_link.sql`

Each container will be available 24h max


```
martin@ubuntu:~/$cat 16-no_link.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password:
score   name
18  Aria
12  Aria
10  John
10  Bob
martin@ubuntu:~/$

```


---


### [17. Go to UTF8](100-move_to_utf8.sql)

Write a script that converts `hbtn_0c_0` database to UTF8 (`utf8mb4`, collate `utf8mb4_unicode_ci`) in your MySQL server.

You need to convert all of the following to `UTF8`:

* Database `hbtn_0c_0`
* Table `first_table`
* Field `name` in `first_table`

**Repo:**

* GitHub repository: `holbertonschool-higher_level_programming`
* Directory: `0x0D-SQL_introduction`
* File: `100-move_to_utf8.sql`

Each container will be available 24h max


```
martin@ubuntu:~/$cat 100-move_to_utf8.sql | mysql -hlocalhost -uroot -p
Enter password:
martin@ubuntu:~/$cat 5-full_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password:
Table   Create Table
first_table CREATE TABLE `first_table` (\n  `id` int(11) DEFAULT NULL,\n  `name` varchar(256) COLLATE utf8mb4_unicode_ci DEFAULT NULL\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
martin@ubuntu:~/$

```


