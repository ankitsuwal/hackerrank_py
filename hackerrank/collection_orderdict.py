from collections import OrderedDict


def order_dict(n_vals, std_marks):
    for _ in range(n_vals):
        value = input().split()
        price = int(value[-1])
        name = ' '.join(value[:-1])
        if std_marks.get(name):
            std_marks[name] += price
        else:
            std_marks[name] = price
    return std_marks


if __name__ == '__main__':
    n = int(input())
    student_marks = OrderedDict()
    student_marks = order_dict(n, student_marks)
    for key in student_marks.keys():
        print(key, student_marks[key])


