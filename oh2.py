#ChoeHB Oh

"""
10
1 2 3 4 5 6 7 8 9 10
13

25
1 3 6 9 13 17 21 23 24 31 37 38 44 45 47 51 55 58 71 73 88 91 99 102
102

40
1 17 19 23 25 28 41 44 49 50 61 64 65 67 71 77 79 81 82 83 84 90 91 92 96 99 101 103 109 121 128 132 133 150 152 161 165 167 177 178
199
"""

n = int(input())
data = tuple(map(int, input().split()))
k = int(input())

# 1번
def rec(start, end):
    if end <= start:
        return 0
    s = data[start] + data[end]
    if s > k:
        return rec(start, end - 1)
    elif s < k:
        return rec(start + 1, end)
    return rec(start + 1, end - 1) + 1

# 2번 - Floor
def floor(start, end):
    
    half = int((start + end) / 2)
    num = data[half]
    num2 = data[half+1]
    
    if start + 1 == end or num == k:
        if k < num: # num과 num2 둘 다 만족 못 하는 경우
            return -1
        return num2 if num2 <= k else num
    
    elif num < k:
        return floor(half, end)

    return floor(start, half) # if k < num


# 3번 - Ceiling
def ceiling(start, end):
    
    half = int((start + end) / 2)
    num = data[half]
    num2 = data[half+1]
    
    if start + 1 == end or num == k:
        if num2 < k: # num과 num2 둘 다 만족 못 하는 경우
            return -1
        return num if k <= num else num2
    
    elif num < k:
        return ceiling(half, end)

    return ceiling(start, half)


# print(rec(0, n-1)) #1번용
print(floor(0, n-1)) #2번용-1
print(ceiling(0, n-1)) #2번용-2

