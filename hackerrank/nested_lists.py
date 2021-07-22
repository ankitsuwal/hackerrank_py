def input_(num):
    data = []
    for i in range(num):
        data.append([input(), float(input())])
    return data


def second_lowest(data):
    second_ = sorted(list(set([marks for name, marks in data])))[1]
    print('\n'.join([name for name, marks in sorted(data) if marks == second_]))


if __name__ == "__main__":
    iter_val = int(input())
    data = input_(iter_val)
    # data = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
    second_lowest(data)
