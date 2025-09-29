# python_learning

## Python最佳实践

Beautiful is better than ugly.

Simple is better than complex.

Complex is better than complicated.

Readability counts.

There should be one-- and preferably only one --obvious way to do it.

Now is better than never.


## Django相关命令

### 建立虚拟环境
 python -m venv ll_env

### 激活虚拟环境（Windows）
 ll_env\Scripts\activate

### 在Django中创建项目
 django-admin startproject ll_project .

### 创建数据库
python manage.py migrate

### 查看项目
python manage.py runserver

### 创建应用程序
python manage.py startapp learning_logs

### 命令 makemigrations 让 Django 确定该如何修改数据库，使其能够存储与前面定义的新模型相关联的数据
python manage.py makemigrations learning_logs

### 要在 Django 中创建超级用户
python manage.py createsuperuser


## 参考书籍---Python编程：从入门到实践

