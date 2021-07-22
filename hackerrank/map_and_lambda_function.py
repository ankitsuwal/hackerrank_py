cube = lambda n: n ** 3  # complete the lambda function


def fibonacci(n):
    # return a list of fibonacci numbers
    a = 0
    b = 1
    sum = 0
    values_list = []
    count = 1
    while count <= n:
        values_list.append(sum)
        count += 1
        a = b
        b = sum
        sum = a + b
    return values_list


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
