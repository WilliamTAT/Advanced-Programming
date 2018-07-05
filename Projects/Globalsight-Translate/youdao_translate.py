# coding=utf-8

'''
- File name: youdao_translate.py
- Description: 实现调用有道翻译API进行翻译
- Function List:
  1. _init_:构造函数接收源语言和目标语言并初始化其他参数
  2. getUrlEncodedData: 将数据进行编码请求有道 API 返回编码后的数据
  3. parseHtml: 解析内容并返回结果
  4. translate: 调用getUrlEncodedData和 parseHtml函数
'''

import urllib.request
import json
import time
import hashlib



class YouDaoFanyi:
    def __init__(self):
        '''
        :description: 构造函数，初始化有道翻译所需参数
        '''
        self.url = 'https://openapi.youdao.com/api/'
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36",
        }
        self.appKey = '23add35e5a6bb158'  # 应用id
        self.appSecret = 'A4fSwvgng3YKuFaWFUWw6I9Aupo9Bivx'  # 应用密钥
        self.langFrom = 'EN'   # 翻译前文字语言,auto为自动检查
        self.langTo = 'zh-CHS'     # 翻译后文字语言,auto为自动检查

    def getUrlEncodedData(self, queryText):
        '''
        :description:将数据进行url编码，并返回编码后的数据
        :param str queryText: 待翻译的文字
        :param str salt: 加密值
        :param str sign: 发送请求的所有数据
        :return str data: 返回url编码后的数据
        '''
        # 产生随机数 ,对用户密码进行加密
        salt = str(int(round(time.time() * 1000)))
        # 先对sign.str进行统一编码，否则报错：Unicode-objects must be encoded before hashing
        sign_str = self.appKey + queryText + salt + self.appSecret
        # 根据用户请求的url参数，生成sign签名
        sign = hashlib.md5(sign_str.encode("utf8")).hexdigest()
        payload = {
            'q': queryText,
            'from': self.langFrom,
            'to': self.langTo,
            'appKey': self.appKey,
            'salt': salt,
            'sign': sign
        }
        data = urllib.parse.urlencode(payload)
        #返回编码后的数据
        return (data)

    def parseHtml(self, html):
        '''
        :description: 解析页面，输出翻译结果
        :param str html: 翻译返回的页面内容
        :return str translationResult: 返回翻译结果
        '''
        #解析页面，返回结果
        data = json.loads(html.decode('utf-8'))
        #将结果赋给translationReasult
        translationResult = data['translation']
        if isinstance(translationResult, list):
            translationResult = translationResult[0]
        # 返回调用api的翻译结果
        return (translationResult)

    def translate(self, queryText):
        '''
        :description: 将 getUrlEncodedData 和 parseHtml 串起来
        :return str self.parseHtml: 返回翻译结果
        '''
        # 获取url编码过的数据
        data = self.getUrlEncodedData(queryText)
        # 构造目标url
        target_url = self.url + '?' + data
        # 构造请求
        request = urllib.request.Request(target_url, headers=self.headers)
        # 发送请求
        response = urllib.request.urlopen(request)
        # 解析，显示翻译结果
        return self.parseHtml(response.read())


'''
if __name__ == "__main__":
    text = 'Perplexity service(s) dependencies found. The perplexity service(s) you are trying to remove is/are part of the GlobalSight objects listed below. You must resolve these dependencies before removing the perplexity service(s). \\n\\n*** Workflow Template(s) *** \\n'
    fanyi = YouDaoFanyi()
    result = fanyi.translate(text)
    print(result)
'''