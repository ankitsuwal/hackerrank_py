def input_(num):
    data = []
    for i in range(num):
        data.append([input(), float(input())])
    return data


def second_lowest(data):
    pass


if __name__ == "__main__":
    iter_val = int(input())
    data = input_(iter_val)
    second_lowest(data)
