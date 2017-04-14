m,n = list(map(int,input().split()))
arr = input().split()
print(' '.join(arr[n:] + arr[:n]))