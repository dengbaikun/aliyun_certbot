#!/bin/bash
set -euo pipefail

echo "================cleanup_hook.sh start============"
export PYTHONPATH=/opt/PythonProject/aliyun_certbot # 修改python 环境目录

echo "$CERTBOT_DOMAIN"  # 域名
PYTHON_HOME=/opt/anaconda3/envs/aliyun_certbot/bin

if [ -f "/tmp/CERTBOT_${CERTBOT_DOMAIN}/RECORD_ID" ]; then
    "${PYTHON_HOME}/python" /opt/PythonProject/aliyun_certbot/certbot_dns/cleanup_hook.py -d "$CERTBOT_DOMAIN"
fi

echo "================cleanup_hook.sh end============"
