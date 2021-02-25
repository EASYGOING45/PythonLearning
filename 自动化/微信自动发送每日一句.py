from __future__ import unicode_literals
from threading import Timer
from wxpy import *
import requests
import  random
import time

#windows执行登录
# bot=Bot()

def get_news():
    '''爬取金山词霸每日一句'''
    url = "http://open.iciba.com/dsapi/"
    r = requests.get(url)
    content=r.json()['content']
    note=r.json()['note']
    print(content)
    print(note)
    return content,note

get_news()


# def send_news():
#     try:
#         contents=get_news()
#         my_friend=bot.friends().search('记得')[0]
#         my_friend.send(contents[0])
#         my_friend.send(contents[1])
#         my_friend.send(u"你好")
#
#         #设置发送时间
#         t=Timer(86400,send_news())
#         ran_int=random.randint(0,100)
#         t=Timer(86400+ran_int,send_news())
#
#         t.start()
#     except:
#
#         my_friend=bot.friends.search('晴川飞马')[0]
#         my_friend.send(u'今天消息发送失败了')
#
# if __name__ =="__main__":
#     send_news()

