import sys
n = int(input().strip())
arr = map(int,input().split())
print(' '.join(map(str,arr[::-1])))
#for i in arr[::-1]:
