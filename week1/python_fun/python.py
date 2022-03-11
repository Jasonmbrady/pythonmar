# for x in range(10):
#     print(x)

# Numbers 10, 12.6, 3.141
# Booleans True, False
# Strings "Literally anything can go in here 10" 

# Variables
all_there_is_to_it = "this is really all there is to it"
my_var = True

# Collections
# List: [ , , , ]
# my_list = ["banana", "apple", "tomato"]
# print(my_list[1])
# Dictionaries: {"key": "value"}
# my_dict = { "name": "Jason Brady", "age": 42, "is_teacher": True}
# print(my_dict["name"])

# Conditionals
# a = 10
# b = 10

# if a > b:
#     print("yup")
# if b > a:
#     print("nope")

# Looping
# while x == "Run":
#     if player_input == " ":
#         x = "Pause"
# for(var i = 0; i < 10; i++){

# }
# for i in range(10): #i will start at 0, and increase by 1 each time.
#     print(i)


# fruits = ["banana", "apple", "tomato"]
# for fruit in fruits:
#     print(fruit)

my_dict = { "name": "Jason Brady", "age": 42, "is_teacher": True, "other_name": ["Jason Brady"]}

for key, value in my_dict.items():
    if value == "Jason Brady":
        print(key)

my_dict['other_name'][0]

all_people = [{"name": "Jason Brady", "age": 42, "is_teacher": True}, {"name": "Alexia", "age": "?", "is_teacher": False}, {"name": "Caden Wilcox", "age": "not 42", "is_teacher": True}]

for person in all_people:
    print(person['is_teacher'])