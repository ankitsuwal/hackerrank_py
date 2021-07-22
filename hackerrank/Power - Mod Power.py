def power_mode(a, b, m):
    print('{0}\n{1}'.format(a**b, pow(a, b, m)))


if __name__ == "__main__":
    a = int(input())
    b = int(input())
    m = int(input())
    power_mode(a, b, m)