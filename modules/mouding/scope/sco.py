# #value changer
# from abc import ABC, abstractmethod
# global x
# x = 10
# @abstractmethod
# def change_value():
#     pass
# def change_value():
#     x = 20
#     print(x)

# change_value()


# # Global vs local
# name = "Global"
# def my_func():
#     name = "local"
#     print(name)
# my_func()
# print(name)

#nonlocal

def outer():
    count = 0
    def inner():
        nonlocal count
        count += 1
    inner()
    inner()
    return count
print(outer())