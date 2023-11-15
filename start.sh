#!/bin/bash
source activate aliyun_certbot
export PYTHONPATH=/opt/PythonProject/aliyun_certbot
python /opt/PythonProject/aliyun_certbot/get_wildcard_cert.py