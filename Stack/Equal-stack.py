n1, n2, n3 = input().strip().split(' ')
n1, n2, n3 = [int(n1), int(n2), int(n3)]
h1 = [int(h1_temp) for h1_temp in input().strip().split(' ')]
h2 = [int(h2_temp) for h2_temp in input().strip().split(' ')]
h3 = [int(h3_temp) for h3_temp in input().strip().split(' ')]

sum1 = sum(h1)
sum2 = sum(h2)
sum3 = sum(h3)

check = sum1 == sum2 == sum3

while not check:

    if sum1 >= sum2 and sum1 >= sum3:
        sum1 -= h1.pop(0)
    elif sum2 >= sum1 and sum2 >= sum3:
        sum2 -= h2.pop(0)
    elif sum3 >= sum1 and sum3 >= sum2:
        sum3 -= h3.pop(0)
    check = sum1 == sum2 == sum3
print(sum1)