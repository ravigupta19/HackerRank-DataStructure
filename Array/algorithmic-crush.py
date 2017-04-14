n,m = map(int,input().split())
l = [0 for _ in range(n+1)]
for _ in range(m):
    a,b,k = map(int,input().split())
    for i in range(a-1,b):
        l[i] += k
print(max(l))