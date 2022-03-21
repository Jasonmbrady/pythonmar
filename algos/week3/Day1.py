def sigma(num):
    sum = 0
    for i in range(num+1):
        sum+=i
    return sum

# TEST CASES
print(sigma(4)) # should return 10
print(sigma(6)) # should return 21
print(sigma(10)) # should return 55