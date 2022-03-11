# def hello():
#     print("Hello, World")
# hello()

# def hello():
#     num_list = []
#     for num in range(10):
#         pizza = 2*num
#         num_list.append(pizza)
#     return num_list
# print(hello())

# Arguments and parameters
def say_hi(name = "Jason", favorite = "pepperoni"):
    return f"Hello, {name}! I hear your favorite pizza topping is {favorite}" 

# def say_hello(name, favorirte):
#     return "Hi, " + name

print(say_hi(favorite="Pepperoni", name="Jason"))
# print(say_hello("Caden"))

