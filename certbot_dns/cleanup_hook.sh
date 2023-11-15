#!/bin/bash
echo "================cleanup_hook.sh start============"
#source activate aliyun_certbot
export PYTHONPATH=/opt/PythonProject/aliyun_certbot #修改python 环境目录
echo $CERTBOT_DOMAIN  #域名
PYTHON_HOME=/opt/anaconda3/envs/aliyun_certbot/bin
if [ -f /tmp/CERTBOT_$CERTBOT_DOMAIN/RECORD_ID ]; then
        RECORD_ID=$(cat /tmp/CERTBOT_$CERTBOT_DOMAIN/RECORD_ID)
        $PYTHON_HOME/python /opt/PythonProject/aliyun_certbot/certbot_dns/auth_hook.py -d $CERTBOT_DOMAIN
        rm -f /tmp/CERTBOT_$CERTBOT_DOMAIN/RECORD_ID
fi
echo "================cleanup_hook.sh end============"