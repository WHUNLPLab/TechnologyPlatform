# 武汉大学语言与信息研究中心-技术演示平台

## 概述

本项目主要利用Docker技术和Flask Web开发技术建设。其中Docker负责部署服务，[Flask](http://www.pythondoc.com/flask-mega-tutorial/) 微框架主要用于快速开发web应用。

开发者需具备基本的Web开发经验，包括语言基础（HTML, CSS, javascript, Python)，MVC软件设计规范以及一般的算法及数据结构素养。

### 项目结构

项目主要分为两个文件夹，分别为`scripts`和`server`，其中`scripts`主要存放服务器运行脚本，开发人员可不理会（部署人员须知），`server`中存放部署的服务端代码。

在`server`中，`website`中存放源代码，如果使用`pycharm`或者其他IDE进行开发，<u>请导入该文件夹</u>。`server`中的其他文件，基本是服务器配置文件。

### 开发流程

1. 导入`website`文件夹作为项目根目录，根据目录内`requirements.txt`安装相应python库。其中`uwsgi`为服务端必须，客户端非必须。
2. 项目源代码主要在`website/application`目录下。其中，`controller`下存放业务逻辑层，`models`下存放模型层，`templates`下存放视图层，`static`下存放静态文件。每个目录下，又根据业务不同分为多个子文件夹，详情请亲自查看。
3. 根目录下的`config.py`为配置文件，主要配置数据库信息。开发过程中，若需要使用本地数据库，请修改配置文件连接数据库。（默认使用sqlite数据库，可下载项目数据库文件放在`website`目录下）
4. 项目运行文件为`manage.py`，实测`pycharm`可以直接运行。如果是其它IDE或者控制台启动，请将运行命令设置为`python manage.py --runserver`。更多选项请是用命令`python manage.py --?`或`python manage.py --help`获取。

### 注意事项

1. 因为项目中`jQuery`符号存在冲突，所有js中的`$`符号请使用`jQuery`全称代替。
2. 如果不熟悉Web开发，请移步[W3School](http://www.w3school.com.cn/)，[Flask](http://flask.pocoo.org/)进行学习。本项目不保证包学包会。

