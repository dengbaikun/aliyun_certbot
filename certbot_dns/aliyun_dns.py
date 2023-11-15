from typing import Union
from utils.logger import logger
from utils.config import global_config
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkalidns.request.v20150109.AddDomainRecordRequest import AddDomainRecordRequest
from aliyunsdkalidns.request.v20150109.DeleteDomainRecordRequest import DeleteDomainRecordRequest


class AliyunDns(object):
    def __init__(self):
        self.appid = global_config.getRaw('aliyun', 'appid')
        self.appsecret = global_config.getRaw('aliyun', 'appsecret')
        self.__letsencryptSubDomain = '_acme-challenge'

    def add_dns_record(self,domain_name_re, domain_name, type, value):
        try:
            client = AcsClient(self.appid, self.appsecret, 'cn-hangzhou')
            request = AddDomainRecordRequest()
            request.set_accept_format('json')
            request.set_Value(value)
            request.set_Type(type)
            request.set_RR(domain_name_re)
            request.set_DomainName(domain_name)
            response = client.do_action_with_exception(request)
            # python2:  print(response)
            response = str(response, encoding='utf-8')
            logger.info(f'response=[{response}]')
            return response
        except Union[ClientException, ServerException] as result:
            logger.info(f'exception=[{result}]')

    def del_dns_record(self, record_id):
        try:
            client = AcsClient(self.appid, self.appsecret, 'cn-hangzhou')
            request = DeleteDomainRecordRequest()
            request.set_RecordId(record_id)
            response = client.do_action_with_exception(request)
            response = str(response, encoding='utf-8')
            logger.info(f'response=[{response}]')
            return response
        except Union[ClientException, ServerException] as result:
            logger.info(f'exception=[{result}]')
