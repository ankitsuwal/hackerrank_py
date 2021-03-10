def split_and_join(line):
    # write your code here
    list_str = line.split(" ")
    line = "_".join(list_str)
    return line

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
