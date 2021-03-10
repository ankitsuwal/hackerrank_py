# def print_full_name(a, b):
#     print('Hello {} {}! You just delved into python.'.format(a, b))
#     # print('I love {} for "{}!"'.format(a, b))
#
#
# if __name__ == '__main__':
#     first_name = input()
#     last_name = input()
#     print_full_name(first_name, last_name)

def print_formatted(number):
    # your code goes here
    for dec in range(1, number+1):
        print(dec, " ", oct(dec), " ", hex(dec), " ", bin(dec))
        # print("{}  {}  {}  {} ".format(dec, oct(dec), hex(dec), bin(dec)))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)