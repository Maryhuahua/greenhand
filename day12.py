""""归并排序"""

def  merge_sort(alist):
    if len(alist)==1:
        return alist
    left_alist = merge_sort(alist[:len(alist)//2])
    right_alist = merge_sort(alist[len(alist)//2:])
    return  merge(left_alist,right_alist)

def merge(left_alist,right_alist):
    left_index ,right_index,merge_alist = 0,0,list()
    while left_index <len(left_alist) and right_index < len(right_alist):
        if left_alist[left_index]<=right_alist[right_index]:
            merge_alist.append(left_alist[left_index])
            left_index+=1
        else:
            merge_alist.append(right_alist[right_index])
            right_index +=1
    merge_alist = merge_alist + left_alist[left_index:] + right_alist[right_index:]
    return merge_alist



my_alist = [12,34,21,65,21,13]
print(merge_sort(my_alist))


"""计数排序"""
def counting(alist):
    if len(alist)<2:
        return alist
    max_num = max(alist)
    count = [0]*(max_num+1)
    for num in alist:
        count[num] +=1
    new_alist = list()
    for i in range(len(count)):
        for j in range(count[i]):
            new_alist.append(i)
    return new_alist
my_alist = [12,34,21,65,21,13]
print(counting(my_alist))











