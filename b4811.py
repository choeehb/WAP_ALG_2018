dp = {}
def rec(w,h):
    if (w,h) in dp.keys():
        return dp[(w,h)]
    if not w:               # w가 없다면
        return 1            # 경우의 수는 1개뿐
    s = rec(w-1,h+1)        # w를 뽑았을 때의 경우의 수
    if h:                   # h가 0개가 아니라면
        s += rec(w, h-1)
    dp[(w,h)] = s
    return s
    

while True:
    n = int(input())
    if n is 0:
        break
    print(rec(n,0))
