_ = input()
no_of_days = 0
stack = []
maxDays = 0
plants = list(map(int,input().split()))
for i in range(len(plants)):
    plant = plants[i]
    mdays = 0
    while len(stack) != 0 and stack[len(stack) - 1][0] >= plant:
        otherPlant = stack.pop()
        mdays = max(otherPlant[1], mdays)
    days = mdays + 1 if len(stack) != 0 else 0
    stack.append( (plant, days) )
    maxDays = max(days, maxDays)
print(maxDays)