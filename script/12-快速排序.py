
def quick_sort(alist, first, last):
    """快速排序，时间复杂度  nlog2(n)"""
    if first >= last:
        return
    mid_value = alist[first]
    low = first
    high = last
    while low < high:
        # hith 左移
        while low < high and alist[high] > mid_value:
            high -= 1
        alist[low] = alist[high]

        while low < high and alist[low] < mid_value:
            low += 1
        alist[high] = alist[low]
        # 从循环退出时， low == high
        alist[low] = mid_value
        # 对low 左边的列表执行快排
        quick_sort(alist,first,low-1)
        # 对low 右边的列表执行快排
        quick_sort(alist,low+1,last)

if __name__ == "__main__":
    li = [9,8,7,6,5,4,3,2,1,45,24,15,26]
    print(li)
    quick_sort(li,0,len(li)-1)
    print(li)