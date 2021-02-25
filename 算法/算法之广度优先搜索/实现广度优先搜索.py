'''
使用队列这种数据结构来实现
在本题中，若某人的姓名以m结尾，那么他是芒果销售商
'''
from collections import deque

graph={}    #图的构建
graph["you"]=["alice","bob","claire"]
graph["bob"]=["anuj","peggy"]
graph["alice"]=["peggy"]
graph["claire"]=["thom","jonny"]
graph["anuj"]=[]
graph["peggy"]=[]
graph["thom"]=[]
graph["jonny"]=[]

search_queue=deque()      #创建一个队列
search_queue+=graph["you"]  #将你的邻居都加入到这个搜索队列中


def person_is_seller(name):
    ''' 在本题中，若某人的姓名以m结尾，那么他是芒果销售商'''
    return name[-1]=='m'

def search(name):
    search_queue=deque()
    search_queue+=graph[name]
    searched=[]       #这个数组用于记录检查过的人
    while search_queue:  # 只要队列不为空
        person = search_queue.popleft()  # 就取出其中的第一个人
        if not person in searched:    #仅当这个人没检查过时才检查，防止陷入无限循环
            if person_is_seller(person):
                print(person + " is a mango seller!")
                return True
            else:
                search_queue += graph[person]
search("you")

