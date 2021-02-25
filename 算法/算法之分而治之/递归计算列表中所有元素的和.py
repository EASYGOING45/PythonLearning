'''
D&C思维：通过递归来逐渐缩小问题规模
需要先明确基线条件和递归条件
'''
def sum(list):
    if list== []:        #基线条件：列表为空
        return 0
    return list[0] + sum(list[1:])
list1=[1,2,3]
print(type(list1))
print(sum(list1))