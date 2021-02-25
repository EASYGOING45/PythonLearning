from __future__ import unicode_literals
from threading import Timer
from wxpy import *
import requests
import  random
import time

def get_sentences():
    '''爬取金山词霸每日一句'''
    url = "http://open.iciba.com/dsapi/"
    r = requests.get(url)
    content = r.json()['content']
    note = r.json()['note']
    return content, note

content=get_sentences()[0]
note=get_sentences()[1]
time_now=time.strftime('%Y.%m.%d',time.localtime(time.time()))

def writeToFile():
    with open("金句.txt", 'a', encoding='utf-8') as f:  # 将句子写入文件，调整编码为'utf-8',添加写模式
        f.write(time_now + '\n')  # 在每一句内容后加上换行符
        f.write(content + '\n')
        f.write(note + '\n')
        f.write('-----------------------------------------------------------------------------'+'\n')


writeToFile()

