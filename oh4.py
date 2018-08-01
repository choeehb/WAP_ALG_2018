from random import random as random

# 선택정렬
def sort_selection(array):
    array = array[:]
    array2 = []
    for i in range(len(array)):
        num_max = 0
        for a in array:
            num_max = max(a, num_max)
        array2.insert(0, num_max)
        array.remove(num_max)
    return array2

# 버블소트
def sort_bubble(array):
    array = array[:]
    length = len(array)
    for i in range(len(array)):
        for j in range(i, len(array)):
            if array[j] < array[i]:
                array[i], array[j] = array[j], array[i]
    return array

# 삽입정렬
def sort_insertion(array):
    array = array[:]
    for i in range(1, len(array)):
        num = array[i]
        array.pop(i)
        for j in range(i):
            if num <= array[j]:
                break
        array.insert(j, num)
        
    num = array[i]
    array.pop(i)
    for j in range(i):
        if num <= array[j]:
            break
    array.insert(j if num <= array[j] else j+1, num)
    return array

# 머지소
def sort_merge(array):
    array = array[:]
    if len(array) == 1:
        return array

    index_half = int(len(array)/2)

    left = sort_merge(array[:index_half])
    right = sort_merge(array[index_half:])
    array = [0] * len(array)
    
    for i in range(len(array)):
        
        if not len(left):
            array[i] = right.pop(0)
            continue
        
        if not len(right):
            array[i] = left.pop(0)
            continue
        
        m = 0
        if left[0] < right[0]:
            m = left.pop(0)
            
        else:
            m = right.pop(0)
            
        array[i] = m
    return array
    
# 퀵 소트
# pivot = last, mid, random
def sort_quick(array, pivot):
    if len(array) < 2:
        return array

    if pivot == "last":
        index = len(array) - 1
    
    elif pivot == "mid":
        m = min(array[0], array[-1], array[int(len(array)/2)])
        if m == array[0]:
            index = 0
        elif m == array[-1]:
            index = -1
        else:
            index = int(len(array)/2)
        
    else:
        index = int(random() * len(array))

    array = array[:]
    num = array.pop(index)
    lower = sort_quick([n for n in array if n <= num], pivot)
    upper = sort_quick([n for n in array if num < n], pivot)
    array = lower + [num] + upper
    return array
    

# 랜덤한 배열 생성
def random_array(size, num_max = 10):
    return [int(random()*num_max) for i in range(size)]

r = random_array(10)

    

