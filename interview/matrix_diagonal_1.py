# name = input()                  # Reading input from STDIN
# print('Hi, %s.' % name)         # Writing output to STDOUT


# Write program for matrix where the diagonal items set with 1, rest all with 0, with the given rows and columns
# Output:
# 3*3 Matrix
# 1 0 1
# 0 1 0
# 1 0 1
# 	6*6 Matrix
# 1 0 0 0 0 1
# 0 1 0 0 1 0
# 0 0 1 1 0 0
# 0 0 1 1 0 0
# 0 1 0 0 1 0
# 1 0 0 0 0 1
# 	4*4 Matrix
# 1 0 0 1
# 0 1 1 0
# 0 1 1 0
# 1 0 0 1


def create_matrix_1(n , m):
    mat = []
    for i in range(n):
        temp = []
        for j in range(m):
            temp.append(0)
        mat.append(temp)
    return mat


def diagonals_should_one(n, m, mat):
    for i in range(n):
        temp = []
        for j in range(m):
            if i == j or (i + j + 1) == n:
                mat[i][j] = 1
            else:
                temp.append(0)
        mat.append(temp)

    print("\nOutput Matrix: ")
    for i in range(n):
        for j in range(m):
            print(mat[i][j], end=" ")
        print()


if __name__ == "__main__":
    n, m = 6, 6
    mat_3 = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]

    mat_4 = [[0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]]
    rows = int(input("Please enter the number of rows: "))
    columns = int(input("Please enter the number of columns: "))

    mat = create_matrix_1(rows, columns)
    # matrix = [[0 for i in range(rows)] for j in range(columns)]
    print("\nInput Matrix: ")
    for i in range(rows):
        for j in range(columns):
            print(mat[i][j], end=" ")
        print()
    diagonals_should_one(rows, columns, mat)
