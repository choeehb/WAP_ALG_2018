
n = int(input())
nums = []
for i in range(n):
    nums.append(int(input()))
    
m = int(n**(1/2)) # m = 그룹핑 수

for i in range(n % m):
    nums.append(nums[-1])

n = len(nums)
count_group = int(n / m) # 그룹 수

grouped_nums = []
for i in range(count_group):
    start = i * m
    end = (i+1)*m
    grouped_nums.append(nums[start:end])
        
min_nums = [min(nums) for nums in grouped_nums]

while True:
    inp = input()
    if inp == '-1':
        break
    
    i, j = map(int, inp.split())
    left = int(i / m)
    right = int(j / m)
    
    min_middle = min_nums[left + 1 : right]
    min_left = nums[i : (left+1)*m]
    min_right = nums[right*m : j+1]
    
    s = []
    s.extend(min_middle)
    s.extend(min_left)
    s.extend(min_right)
    
    print(min(s))
    
    
    

