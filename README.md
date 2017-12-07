uwsgi-nginx-flask
python3.6


how to run:

git clone
You should now have a directory structure like:
.
├── app
│   └── main.py
└── Dockerfile
Go to the project directory (in where your Dockerfile is, containing your app directory)
Build your Flask image:
docker build -t myimage .
Run a container based on your image:
docker run -d --name mycontainer -p 80:80 myimage

登上浏览器 输入地址就可以访问了！比如: http://192.168.1.100/（此地址是你宿主主机的IP，由容器的端口映射到主机的端口达成！）
