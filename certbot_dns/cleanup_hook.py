# coding=utf-8
import getopt
import os
import sys
from certbot_dns.aliyun_dns import AliyunDns
from utils.logger import logger


def cleanup(certbot_domain):
    print(f'certbot_domain={certbot_domain}')
    record_id_file = f'/tmp/CERTBOT_{certbot_domain}/RECORD_ID'
    if not os.path.exists(record_id_file):
        logger.info(f'未发现待清理记录文件: {record_id_file}')
        return
    with open(record_id_file) as f:
        record_id = f.read()
    aliyun_dns = AliyunDns()
    aliyun_dns.del_dns_record(record_id)
    os.remove(record_id_file)
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
