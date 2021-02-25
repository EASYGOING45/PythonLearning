'''
图由节点和边构成
每个节点都与邻近节点相连
可以通过散列表实现映射关系
'''
graph={}
graph["you"]=["alice","bob","claire"]
graph["bob"]=["anuj","peggy"]
graph["alice"]=["peggy"]
graph["claire"]=["thom","jonny"]
graph["anuj"]=[]
graph["peggy"]=[]
graph["thom"]=[]
graph["jonny"]=[]
'''
注：键-值对的添加顺序重要吗？ Does it matter？
Not at all！ 散列表是映射关系 是无序的
'''
