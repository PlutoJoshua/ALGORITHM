a = int(input())

for i in range(1, a+1):
    b,c = map(int, input().split())
    if b >= c:
        print('MMM BRAINS')
    else:
        print('NO BRAINS')