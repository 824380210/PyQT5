DB

```
[root@test ~]# yum install mariadb-server -y
Loaded plugins: langpacks, product-id, search-disabled-repos, subscription-manager
This system is not registered to Red Hat Subscription Management. You can use subscription-manager to register.
base                                                                                                                                  | 4.1 kB  00:00:00
...

Transaction test succeeded
Running transaction
  Installing : 1:mariadb-5.5.52-1.el7.x86_64                                                                                                             1/3
  Installing : perl-DBD-MySQL-4.023-5.el7.x86_64                                                                                                         2/3
  Installing : 1:mariadb-server-5.5.52-1.el7.x86_64                                                                                                      3/3
  Verifying  : 1:mariadb-server-5.5.52-1.el7.x86_64                                                                                                      1/3
  Verifying  : perl-DBD-MySQL-4.023-5.el7.x86_64                                                                                                         2/3
  Verifying  : 1:mariadb-5.5.52-1.el7.x86_64                                                                                                             3/3

Installed:
  mariadb-server.x86_64 1:5.5.52-1.el7

Dependency Installed:
  mariadb.x86_64 1:5.5.52-1.el7                                              perl-DBD-MySQL.x86_64 0:4.023-5.el7

Complete!
[root@test ~]#

```
# 修改配置，添加16，17行内容

```
[root@test ~]# nl /etc/my.cnf
     1  [mysqld]
     2  datadir=/var/lib/mysql
     3  socket=/var/lib/mysql/mysql.sock
     4  # Disabling symbolic-links is recommended to prevent assorted security risks
     5  symbolic-links=0
     6  # Settings user and group are ignored when systemd is used.
     7  # If you need to run mysqld under a different user or group,
     8  # customize your systemd unit file for mariadb according to the
     9  # instructions in http://fedoraproject.org/wiki/Systemd

    10  [mysqld_safe]
    11  log-error=/var/log/mariadb/mariadb.log
    12  pid-file=/var/run/mariadb/mariadb.pid

    13  #
    14  # include all files from the config directory
    15  #
    16  character-set-server=utf8
    17  datadir=/var/lib/mysql
    18  !includedir /etc/my.cnf.d

```


# 开启服务

```
[root@test ~]#  systemctl start mariadb

```
# 

# 在客户端安装mysqlclient包 

```

C:\Users\pengcz1>pip install mysqlclient
Collecting mysqlclient
  Downloading https://files.pythonhosted.org/packages/32/4b/a675941221b6e796efbb48c80a746b7e6fdf7a51757e8051a0bf32114471/mysqlclient-1.3.12-cp36-cp36m-win_amd64.whl (1.3MB)
    100% |████████████████████████████████| 1.3MB 33kB/s
Installing collected packages: mysqlclient
Successfully installed mysqlclient-1.3.12
You are using pip version 9.0.3, however version 10.0.1 is available.
You should consider upgrading via the 'python -m pip install --upgrade pip' command.

C:\Users\pengcz1>

```

### 如果客户端没有授权连接到服务器端

```
C:\Users\pengcz1\AppData\Local\Programs\Python\Python36\python.exe D:/pyqt5/a/33connectDB.py
(1130, "Host '10.96.199.120' is not allowed to connect to this MariaDB server")

Process finished with exit code 1

```
## 解决方法

```
[root@test ~]# mysql -u root -p
Enter password: ===pass1234
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 31
Server version: 5.5.52-MariaDB MariaDB Server

Copyright (c) 2000, 2016, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> 
MariaDB [(none)]> use mysql
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
MariaDB [mysql]> show tables;
+---------------------------+
| Tables_in_mysql           |
+---------------------------+
| columns_priv              |
| db                        |
|...

| time_zone_name            |
| time_zone_transition      |
| time_zone_transition_type |
| user                      |
+---------------------------+
24 rows in set (0.00 sec)


MariaDB [mysql]> GRANT ALL PRIVILEGES ON *.* TO 'root'@'10.96.199.120' IDENTIFIED BY 'mypass' WITH GRANT OPTION;
Query OK, 0 rows affected (0.00 sec)

MariaDB [mysql]>  flush privileges;
Query OK, 0 rows affected (0.00 sec)

MariaDB [mysql]>

```
##  以上方法可以解决远程访问某个数据库的问题
##  @ 后面的IP 可以用 %代替，如代替后面的部分相当允许某个网段，如果只有一个%相当所有外网

```
[root@test data3]# mysql -u root -p
Enter password:
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 43
Server version: 5.5.52-MariaDB MariaDB Server

Copyright (c) 2000, 2016, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> use mysql
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
MariaDB [mysql]> GRANT ALL PRIVILEGES ON *.* TO 'root'@'10.96.%.%' IDENTIFIED BY 'mypass' WITH GRANT OPTION;
Query OK, 0 rows affected (0.00 sec)

MariaDB [mysql]>  flush privileges;
Query OK, 0 rows affected (0.00 sec)

MariaDB [mysql]>

```


