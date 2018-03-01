__author__ = 'beimenchuixue'
__blog__ = 'http://www.cnblogs.com/2bjiujiu/'
__date__ = '2018/3/1 11:44'

import requests
import json


class YunPian(object):
    """
    发送短信验证码，项目上线必须把服务器的IP添加到白名单中，百度搜索本地IP，将会获取IP地址信息
    """
    def __init__(self, apikey):
        self.apikey = apikey
        self.single_send_url = 'https://sms.yunpian.com/v2/sms/single_send.json'

    def send_sms(self, code, mobile):
        params = {
            'apikey': self.apikey,
            'mobile': mobile,
            'text': '【德玛科技】验证码是{code}。如非本人操作，请忽略本短信'.format(code=code),
        }
        response = requests.post(self.single_send_url, data=params)
        response_dict = json.loads(response.text)
        # 返回状态
        return response_dict


if __name__ == '__main__':
    yun_pain = YunPian('b1d45af7f60a69881ec49ac396b93a7d')
    yun_pain.send_sms(mobile='15570911036')