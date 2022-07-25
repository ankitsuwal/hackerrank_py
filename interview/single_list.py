# Program: 1
lst1 = [1, 2, 3]
lst2 = [4, 5, 6]
output = [(1, 4), (2, 5), (3, 6)]

length = len(lst1) if len(lst1) > len(lst2) else len(lst2)
print("length: ", length)
output = []
for i in range(length):
    output.append((lst1[i], lst2[i]))
print("OUtput: ", output)
# ==================================================================
# Program: 2
# TODO: Testcases: test for all even and odd numbers
ls1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# op = [[1], [2,3], [4,5,6], [7,8,9,0]]

ls2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# op = [[1], [2,3], [4,5,6], [7,8,9]]

ls3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# op = [[1], [2,3], [4,5,6], [7,8,9,10], [11,12,13]]


def con_lst(inp):
    final_lst = []
    start = 0
    end = 1
    for i in range(len(inp)):
        final_lst.append(list(inp[start:end]))
        start = end
        end = end + i + 2
    res = list(filter(None, final_lst))
    print("res: ", res)
    # print("final_lst: ", final_lst)


con_lst(ls3)

