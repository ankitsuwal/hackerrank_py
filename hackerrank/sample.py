# def harmonic(n):
# 	for i in range(1, 4):
#   		print(str(1/i), end='')
#
# n=4
# harmonic(n)

# def deco(func):
#     # print("decorator string: ", name_str)
#     def inner(name_str):
#         print("your are enter the fun")
#         func(name_str)
#         print("after excecution")
#     return inner
#
# @deco
# def main_func(name_str):
#     print("main function: ", name_str)
#     # return name_str
# name_str = "ankit suwal"
# main_func(name_str)

string_val = "maam"
if string_val == string_val[::-1]:
	print("is palindrom")
else:
	print("not palindorm")