# SQLite Database

**Installation**

`$ sudo apt install sqlite3`

**Starting SQLite**

`$ sqlite3`

**Creating Table**

`create table users (id integer primary key autoincrement, name text, location text);`

Basic Format: _create table tablename (column1_name datatype, column2_name datatype)_

**Inserting Row**

`insert into users (name, location) values ('Dipon','Chittagong'); `

**Checking All Tables**

`.tables`

**Exiting from sqlite**

`.quit`
