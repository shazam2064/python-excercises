# >>> cursor.execute('''create table mystaff.employees
#       (id int primary key not null,
#        first_name varchar(25) not null,
#        last_name varchar(25) not null,
#        department varchar(25) not null,
#        phone varchar(25),
#        address varchar(50),
#        salary int);''')
# Traceback (most recent call last):
#   File "<pyshell#8>", line 1, in <module>
#     cursor.execute('''create table mystaff.employees
# psycopg2.errors.InFailedSqlTransaction: current transaction is aborted, commands ignored until end of transaction block
# >>>
# >>> connection.rollback()
# >>> cursor.execute('''create table mystaff.employees
#       (id int primary key not null,
#        first_name varchar(25) not null,
#        last_name varchar(25) not null,
#        department varchar(25) not null,
#        phone varchar(25),
#        address varchar(50),
#        salary int);''')
# >>>
