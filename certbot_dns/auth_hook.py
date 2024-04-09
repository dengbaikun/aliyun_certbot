# coding=utf-8
import getopt
import os
import sys
import json
import time
from certbot_dns.aliyun_dns import AliyunDns
from utils import domain_name_tool
from utils.logger import logger
from certbot_dns import cleanup_hook


def mk_dir(directory):
    d = os.path.exists(directory)
    if not d:
        os.mkdir(directory)
        return True


def auth(certbot_validation, certbot_domain):
    print(f'certbot_validation={certbot_validation},certbot_domain={certbot_domain}')
    # 判断是否存在 存在则删除记录
    try:
        if os.path.exists(f'/tmp/CERTBOT_{certbot_domain}/RECORD_ID'):
            logger.info("存在删除记录")
            cleanup_hook.cleanup(certbot_domain)
    except Exception as e:
        logger.error('添加记录失败',e)

    aliyun_dns = AliyunDns()
    directory = f'/tmp/CERTBOT_{certbot_domain}'
    __letsencryptSubDomain = '_acme-challenge'
    type = 'TXT'
    response_json = aliyun_dns.add_dns_record(domain_name_re='_acme-challenge', domain_name=certbot_domain, type=type,
                                              value=certbot_validation)
    record_id = json.loads(response_json)['RecordId']
    mk_dir(directory)
    with open(f'{directory}/RECORD_ID', 'w', encoding='utf-8') as f:
        f.write(record_id)
    retry_count = 100
    while retry_count > 1:
        text = ''
        try:
            text = domain_name_tool.getTvalue(f'{__letsencryptSubDomain}.{certbot_domain}')
        except Exception as e:
            logger.info(f"获取{certbot_domain} txt记录失败:", e)
        if text == certbot_validation:
            logger.info(f"{certbot_validation}:验证成功")
            break
        retry_count = retry_count - 1
        time.sleep(5)


def main(args):
    certbot_validation = ""
    certbot_domain = ""
    options, arguments = getopt.getopt(args, '-d:-t:', ['certbot_domain=', 'certbot_validation='])
    for opt_name, opt_value in options:
        if opt_name in ('-d', '--certbot_domain'):
            certbot_domain = opt_value
        if opt_name in ('-t', '--certbot_validation'):
            certbot_validation = opt_value
    auth(certbot_validation, certbot_domain)


if __name__ == '__main__':
    main(sys.argv[1:])
