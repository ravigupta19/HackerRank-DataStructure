import sys
arr = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)
largest_sum = None
for arr_i in range(4):
    for arr_j in range(4):
        A = arr[arr_i][arr_j:arr_j+3]
        B = [arr[arr_i+1][arr_j+1]]
        C = arr[arr_i+2][arr_j:arr_j+3]
        total = sum(A+B+C)
        if largest_sum == None:
            largest_sum = total
        elif total > largest_sum:
            largest_sum = total
print(largest_sum)





