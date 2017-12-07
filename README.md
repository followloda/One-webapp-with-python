#one app with flask
uwsgi-nginx-flask python3.6


##how to run:

-git clone

-创建镜像: docker build -t flask-app-image .

-运行容器: docker run -d --name flaskapp -p 80:80 flask-app-image

-登上浏览器 输入地址就可以访问了！比如: http://192.168.1.100/（此地址是你宿主主机的IP，由容器的端口映射到主机的端口达成！）


----
##ToDoList
-添加用户认证
-前端页面展示
-数据库
-添加定时爬取图片
