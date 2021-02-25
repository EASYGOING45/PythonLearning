'''
这是一个查重函数
判断这个人是否存在
'''
vote=dict()
vote["Jack"]=True
vote["Tom"]=True
def check_voter(name):
    if vote.get(name):
        print("Kick them out")
    else:
        vote[name]=True
        print("Let them vote")
print(check_voter("Amy"))