# 图书管理系统
## 环境:python3.7,Django2.1.7,数据库:mysql5.7,pymysql 0.9.3, win10,前端样式为Bootstrap v3.3.7,jQuery v3.3.1
### 项目演示:[图书管理系统](http://bms.cxmgxj.cn "图书管理系统")
### 基本功能介绍:
    - 出版社,书籍,作者的增删改查 
	- 删除作者或出版社时,通过ajax渲染模态框提示是否删除依赖其关系的书籍数据.
### 如何开始:
    - git clone git@github.com:swpu-cxm/bms.git
    - cd bms
    - pipenv install
    - pipenv shell
    - 调整bms/settings.py中数据库配置
    - python manager.py makemigrations
    - python manager.py migratie
    - python manager.py runserver
