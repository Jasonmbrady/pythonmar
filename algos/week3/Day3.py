# Write a function that takes in a list and reverses the order of the values. For example the list [1,2,3,4,5] would return [5,4,3,2,1].  SENSEI BONUS - Work in place (don't create a new array).

# Basic Approach
def reverse_list_basic(list):
    new_list = []
    for i in range(len(list)-1, -1, -1):
        new_list.append(list[i])
    return new_list

# Test Cases
print(reverse_list_basic([1,2,3,4]))
print(reverse_list_basic([8,6,7,5,3,0,9]))

# Sensei Approach
def reverse_list_sensei(list):
    temp = None
    for i in range(len(list)-1):
        if i < len(list)-(i+1):
            temp = list[i]
            list[i] = list[-(i+1)]
            list[-(i+1)] = temp
    return list

# Test Cases
print(reverse_list_sensei([1,2,3,4]))
print(reverse_list_sensei([8,6,7,5,3,0,9]))