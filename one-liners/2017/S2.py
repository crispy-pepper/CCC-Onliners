n = int(input())
tides,mid = sorted(list(map(int,input().split()))),n//2 if n%2==0 else n//2+1
low,high=sorted(tides[:mid],reverse=True),sorted(tides[mid:])
result = [None]*(n)
result[::2] = low
result[1::2] = high

print(*result)