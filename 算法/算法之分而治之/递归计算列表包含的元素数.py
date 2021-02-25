def count(list):
    if list == []:
        return 0
    return 1+count(list[1:])
print("递归求列表元素个数")
list1=[1,5,8,9,10]
print(count(list1))