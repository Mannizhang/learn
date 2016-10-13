# MYSQL

**目前动态网站都是基于数据库，将网站内容使用数据库管理系统去管理的**

**用户、栏目、图片、文章、评论都存在数据库之中**
### 为什么选择MYSQL
- 数据库种类有很多：Oracle/DB2/SQL serve
- PHP+MYSQL 是黄金搭档 大多数网站都是这么搭的
- MYSQL的最大的优点：支持所有系统



### MYSQL的架构
- c/s 客户端+服务器
- 在客户端操作服务器,服务器管理数据库，数据库里面有行有列（行是指记录，列是指字段）
- 客户端执行的命令发送到软件，软件替我们执行命令，随着命令的操作将结果返回到客户端
- ps：可以在不同的电脑里面安装客户端，但是MYSQL为了安全不会支持远程连接


##PHP程序员主要学习那些数据库的操作:
- 为我的项目设计表（合理的建立表与表的关系）
- 使用SQL语句
- 其他的可以用工具解决

##启动语句
- CMD操作MYSQL:net stop mysql 
             net start mysql
- 操作服务器：service mysql start/stop/restart

## MYSQL目录结构（重要的有三个）
- 目录方面的了解：bin：存MYSQL的所有命令
- data：库（一个目录一个库）在库的目录里面新建一个文件夹就是新建一个库
- 还有my.ini配置文件（在里面可以改变端口，还可以改变路径）


## 了解数据库的SQL语句操作（重点内容）
- 操作指令SQL结构查询语言分为四大类
    1.DDL定义、管理数据库对象（创库创表）
    2.DML对数据集的操作（插入、更新、消除）
    3.DQL查询
    4.DCL数据控制语言（权限&数据的更改）
### 1.执行SQL语句，连接到数据库服务器
- mysql -h localhost -u root -p(然后会弹出password)
   为了安全管理员用root作为名字，在本机只留一个账户和密码
- 查状态
   \s
- 查看所有变量
    show variables
    ;
- 查看部分变量
    show variables like' '；


### 2.创建库：
- 创建库之前先执行show databases看系统默认有多少库
- 创建库：create databases 库名；/ create database if not exists； 库名（最好是这样创建）
- 删除库: drop database 库名；/drop database if exist 库名；（最好是这样删除）

### 3.选择一个库作为默认的数据库
- 改默认的库：use 库名
- 库里面创建表
  create table 库 users <id int,name char<30>>;
- 看所有的表
  show tables;
- 看表结构
  desc users;
- 删除表
  drop table if exists users；

### 对表里的数据进行增删改查
- 插入数据：insect into 表名 value<>；
- 插入部分字段：insect into 表名<   ,   ,   ,    ,   >value<"   ">；(用字符串的方式写)
- 查看数据：select *from（表名）；
- 更新：update 表名 set name='自己写 '   where id='自己写  ' ;
     同时改几项，用逗号隔开
- 删除 delete from 表名 where id='   ';

### 帮助的使用：？ contents



