#!/bin/bash
set -euo pipefail

echo "================auth_hook.py start============"
echo "$CERTBOT_VALIDATION" # txt校验值
echo "$CERTBOT_DOMAIN"  # 域名

export PYTHONPATH=/opt/PythonProject/aliyun_certbot
PYTHON_HOME=/opt/anaconda3/envs/aliyun_certbot/bin # 修改python 环境目录

"${PYTHON_HOME}/python" --version
"${PYTHON_HOME}/python" /opt/PythonProject/aliyun_certbot/certbot_dns/auth_hook.py -d "$CERTBOT_DOMAIN" -t "$CERTBOT_VALIDATION"

echo "================auth_hook.py end============"
