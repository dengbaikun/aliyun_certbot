# 证书申请 支持阿里云脚本使用  certbot

资料

```shell
https://www.digitalocean.com/community/tools/nginx?global.nginx.nginxConfigDirectory=%2Fusr%2Flocal%2Fnginx%2F&global.nginx.workerProcesses=4&global.nginx.user=dk&global.nginx.clientMaxBodySize=50&global.app.lang=zhCN
https://snapcraft.io/docs/installing-snap-on-centos
https://certbot.eff.org/instructions?ws=nginx&os=centosrhel7
https://eff-certbot.readthedocs.io/en/stable/using.html#webroot
```

安装步骤

```shell
sudo yum install snapd
sudo systemctl enable --now snapd.socket
sudo ln -s /var/lib/snapd/snap /snap
sudo snap install core
sudo snap refresh core
sudo snap install --classic certbot
sudo ln -s /snap/bin/certbot /usr/bin/certbot
certbot --server https://acme-v02.api.letsencrypt.org/directory --key-type ecdsa --elliptic-curve  secp384r1 --rsa-key-size 4096 --email dengbaikun@foxmail.com --cert-name example.com  -d "*.example.com" -d  "example.com" --manual --preferred-challenges certbot_dns-01 certonly
```
按照提示在域名解析那里 添加txt  _acme-challenge值 进行检验
下面有提供全动态化申请https证书demo

删除证书

```shell
certbot delete --cert-name example.com
```

吊销证书

```shell
certbot revoke --cert-name example.com
```

申请https证书demo
使用环境是python3.7
config.ini 填写阿里云 AccessKey appid appsecret 以及要申请证书域名
![config.ini配置文件
](https://img-blog.csdnimg.cn/06740d8b18854501bbe3dbdeb558456c.png)
修改hook shell脚本python 环境目录
![在这里插入图片描述](https://img-blog.csdnimg.cn/4cca3a55240e44bc8e9e85ed249276ab.png)
把代码下载下来使用python3.7环境
安装包
pip install -r requirements.txt
执行
sh start.sh就可以了 具有有问题可以提出
代码
