# -*- coding: utf-8 -*-

'''
- File name: youdao_translate.py
- Author: Yang Ruoyao
- Description: 正则表达式提取globalsight资源文件内容，并调用有道翻译API进行翻译，输出中文资源文件
- Function List:
  1. globalsight_translate: 正则表达式提取globalsight资源文件内容，并调用有道翻译API进行翻译，输出中文资源文件
  2. __main__: 调用globalsight_translate函数
'''

import re, string
import youdao_translate as yd


def globalsight_translate(t2):
    '''
    :description: 正则表达式提取globalsight资源文件内容，并调用有道翻译API进行翻译，输出中文资源文件
    :param YouDaoFanyi t2: 有道翻译API实例
    '''
    # 初始化存储翻译结果的列表
    all_results=[]
    pattern1 = r'([a-zA-Z_.0-9]+[\s]*=)([\s]*[0-9a-zA-Z_\W]+)'  # 匹配 x=y模式
    pattern2 = r'[\/]*[a-zA-Z_\-]+(\/)[a-zA-Z\/\-_]+(.gif)'  # 匹配以.gif结尾的路径
    pattern3 = r'[\/]*[a-zA-Z_\-]+(\/)[a-zA-Z0-9.()\/\-_]+(.htm)'  # 匹配以.htm结尾的路径
    pattern4 = re.compile(r'\<[0-9a-zA-Z\s_=.@""\:\(\)\;\/\\]+\>')  # 匹配html标签
    
    i = 1
    with open('LocaleResource_en_US.properties',"r", encoding="utf-8") as f1:
        for line in f1:
            # 匹配 x = y模式的行
            s = re.match(pattern1,line)
            if s is not None:
                # s1=x, x2=y
                s1 = s.group(1)
                s2 = s.group(2)
                # 判断等号右边不是空的，是空的有道翻译API会报错
                if s2.strip()!='':
                    # 如果s2=文件名，则跳过翻译，直接写入文件
                    match2 = re.match(pattern2,s2.strip())
                    match3 = re.match(pattern3,s2.strip())
                    if not match2 and not match3:
                        # s2去除\n,\r,\t
                        s2 = s2.replace('\\n','换换1行行')
                        s2 = s2.replace('\\r','换换2行行')
                        s2 = s2.replace('\\t','换换3行行')
                        matches4 = pattern4.findall(s2)
                        j = -1
                        # 替换s2中的每一个html标签
                        for match4 in matches4:
                            j = j + 1
                            s2 = s2.replace(match4,'标标'+str(j)+'签签')
                        #调用有道翻译API
                        s2 = t2.translate(s2)
                        # 将html标签还原
                        if j>=0:
                            for k in range(j+1):
                                s2 = s2.replace('标标'+str(k)+'签签',matches4[k])
                        # 将\n,\r,\t还原
                        s2 = s2.replace('换换1行行','\\n')
                        s2 = s2.replace('换换2行行','\\r')
                        s2 = s2.replace('换换3行行','\\t')
                print(str(i)+':\t'+s1+s2)
                # 将翻译好格式正确的行先添加入列表
                all_results.append(str(i)+':\t'+s1+s2)
            i += 1
            #if i==6322:
            #    break
    f1.close()
    
    # 循环结束后统一写入文件
    with open('LocaleResource_zh_CN.properties', "w", encoding="utf-8") as f2:
        for result in all_results:
            f2.write(result+'\n')
    f2.close()
    return



if __name__ == "__main__":
    # 创建有道翻译API类的实例
    t2 = yd.YouDaoFanyi()
    # 调用函数进行网站资源文件翻译
    globalsight_translate(t2)