# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 23:25:43 2018

@author: dell
"""

import re

article = ""
for i in range(1,6):
    name = 'corpara/{}.txt'.format(i)
    f = open(name,'r')
    for line in f:
        article += line;
    f.close()

#都转换为小写
article = article.lower()

wordlist = {}
preWords = re.split(r"\W+",article)
for word in preWords:
    if word not in wordlist and word: #排除''
        wordlist[word] = 1
    elif word in wordlist:
        wordlist[word] += 1

#以value值做比较参数进行items的排序(频率由低到高)
sortedList = sorted(wordlist.items(),key = lambda item:item[1])

#将wordlist写入文件
f = open('wordlist.txt','w')
f.write('freq*\tword\n-----\t-----\n')
for line in sortedList:
    f.write(str(line[1])+'\t'+line[0]+'\n')
f.close()

#打印
print('频率最高的前10：')
print("freq*\tword")
print("-----\t-----")
for line in sortedList[-1:-11:-1]:
    print(str(line[1]) + '\t' + line[0])

print('\n频率最低的前10：')
print("freq*\tword")
print("-----\t-----")
for line in sortedList[0:10]:
    print(str(line[1]) + '\t' + line[0])    