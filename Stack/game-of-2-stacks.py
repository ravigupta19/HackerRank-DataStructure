n,m,x = input().strip().split(' ')
n,m,x = [int(n),int(m),int(x)]
a = list(map(int, input().strip().split(' ')))
b = list(map(int, input().strip().split(' ')))
total = 0
count = 0
while total < x:
    if a[0] < b[0]:
        c = a.pop(0)
        total += c
        count += 1
    else:
        d = b.pop(0)
        total += d
        count += 1
print(count-1)
#5 4 10
#4 2 4 6 1
#2 1 8 5
