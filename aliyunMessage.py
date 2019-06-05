#!/usr/bin/env python
#coding=utf-8
# 需要安装阿里云SDK
# pip install aliyun-python-sdk-core-v3
import json
import random

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest
client = AcsClient('<AccessKeyId>', '<AccessKeySecret>', 'default')

def send_sms(phone_number, code):
    request = CommonRequest()
    request.set_accept_format('json')
    request.set_domain('dysmsapi.aliyuncs.com')
    request.set_method('POST')
    request.set_protocol_type('https')  # https | http
    request.set_version('2017-05-25')
    request.set_action_name('SendSms')

    request.add_query_param('PhoneNumbers', phone_number)
    request.add_query_param('SignName', "cvxmbn管理系统")       # 模板名称
    request.add_query_param('TemplateCode', "SMS_166485999")    # TemplateCode
    request.add_query_param('TemplateParam', json.dumps(code))  # 需要将字典转换为json格式

    response = client.do_action_with_exception(request)
    # python2:  print(response)
    return str(response, encoding='utf-8')

if __name__ == '__main__':
    num = 17371039830
    # 生成随机4位验证码
    params = {
        'code': random.randint(1000,9999),
    }
    result = send_sms(phone_number=num, code=params)
    print(result)



