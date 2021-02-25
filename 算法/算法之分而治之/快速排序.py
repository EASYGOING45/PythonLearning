'''
快速排序
时间复杂度：o(n*logn)
'''
def quicksort(array):
    if len(array)<2:
        return array
    else:
        pivot=array[0]   ##将数组的第一个元素设置为基准值
        less=[i for i in array[1:] if i <= pivot]       #由所有小于基准值的元素组成的子数组
        greater=[i for i in array[1:] if i > pivot]     #由所有大于基准值的元素组成的子数组
        return quicksort(less)+[pivot]+quicksort(greater)
print("快速排序算法")
print(quicksort([7,1,9,4,100]))