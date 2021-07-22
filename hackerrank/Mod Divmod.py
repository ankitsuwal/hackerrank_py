def print_integeres(a, b):
    # print("{}", "\n",  "{}",  "\n", "{}", a//b, a % b, divmod(a, b))
    print('{0}\n{1}\n{2}'.format(a//b, a % b, divmod(a, b)))
    # print(a % b)
    # print(divmod(a, b))


if __name__ == "__main__":
    a = int(input())
    b = int(input())
    print_integeres(a, b)
