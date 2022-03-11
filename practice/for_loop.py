# Set 3 variables
# low_num, high_num, mult
# for loop, start at low_num, go through high_num, print when num % 3 == 0
low_num = 2
high_num = 9
mult = 3
for num in range(low_num, high_num):
    if num % 3 == 0:
        print(num)