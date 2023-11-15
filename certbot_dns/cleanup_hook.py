# coding=utf-8
import getopt
import os
import sys
import json
import time
from certbot_dns.aliyun_dns import AliyunDns
from utils.domain_name_tool import getTvalue
from utils.logger import logger


def cleanup(certbot_domain):
    print(f'certbot_domain={certbot_domain}')
    with open(f'/tmp/CERTBOT_{certbot_domain}/RECORD_ID') as f:
        record_id = f.read()
    aliyun_dns = AliyunDns()
    aliyun_dns.del_dns_record(record_id)
    os.remove(f'/tmp/CERTBOT_{certbot_domain}/RECORD_ID')
    logger.info(f"record_id:{record_id},删除改{record_id}dns成功")


def main(args):
    certbot_domain = ""
    options, arguments = getopt.getopt(args, '-d:', ['certbot_domain='])
    for opt_name, opt_value in options:
        if opt_name in ('-d', '--certbot_domain'):
            certbot_domain = opt_value
    cleanup(certbot_domain)


if __name__ == '__main__':
    main(sys.argv[1:])
