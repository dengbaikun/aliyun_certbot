#!/bin/bash
echo "================auth_hook.py start============"
echo $CERTBOT_VALIDATION #txt校验值
echo $CERTBOT_DOMAIN  #域名
#source activate aliyun_certbot
export PYTHONPATH=/opt/PythonProject/aliyun_certbot
PYTHON_HOME=/opt/anaconda3/envs/aliyun_certbot/bin #修改python 环境目录
$PYTHON_HOME/python --version
type /opt/anaconda3/envs/aliyun_certbot/bin/python
/opt/anaconda3/envs/aliyun_certbot/bin/python /opt/PythonProject/aliyun_certbot/certbot_dns/auth_hook.py -d $CERTBOT_DOMAIN -t $CERTBOT_VALIDATION
echo "================auth_hook.py end============"
## Sleep to make sure the change has time to propagate over to DNS
#sleep 25