import re
Pattern = re.compile("(0/91)?[7-9][0-9]{9}")


def valid_mob(nums):
    for num in nums:
        if len(num) == 10 and num.isdigit():
            if Pattern.match(num):
                print("YES")
            else:
                print("NO")
        else:
            print("NO")


if __name__ == '__main__':
    n = int(input())
    num_ = list()
    for index in range(n):
        num = input()
        num_.append(num)
    valid_mob(num_)


# N = int(input())
#
# for i in range(N):
#     number = input()
#     if(len(number)==10 and number.isdigit()):
#         output = re.findall(r"^[789]\d{9}$",number)
#         if(len(output)==1):
#             print("YES")
#         else:
#             print("NO")
#     else:
#         print("NO")