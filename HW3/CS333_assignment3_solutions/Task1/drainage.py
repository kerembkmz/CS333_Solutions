import sys
def read_file(filename):
    try:
        with open(filename) as file:
            contents = file.readlines()
            return contents
    except:
        print("File read failed.")

def ParseContent(contents):
    row, column = map(int, contents[0].strip().split())
    matrix = []
    for line in contents[1:]:
        data = list(map(float, line.strip().split()))
        matrix.append(data)

    return row, column, matrix


def print_matrix(matrix):
    for line in matrix:
        print(line)


def matrix_has_no_flow(matrix, i, j):
    row_num = len(matrix)
    col_num = len(matrix[0])
    matrix_has_down_cell = (i+1 < row_num)
    matrix_has_up_cell = (i-1 >= 0)
    matrix_has_right_cell = (j+1 < col_num)
    matrix_has_left_cell = (j-1 >= 0)

    if ((not matrix_has_down_cell or matrix[i][j] <= matrix[i + 1][j]) and
            (not matrix_has_up_cell or matrix[i][j] <= matrix[i - 1][j]) and
            (not matrix_has_left_cell or matrix[i][j] <= matrix[i][j - 1]) and
            (not matrix_has_right_cell or matrix[i][j] <= matrix[i][j + 1])):
        return True


def find_max_opt_neighbor(matrix, OPT, i, j):
    row_num = len(OPT)
    col_num = len(OPT[0])
    matrix_has_down_cell = (i + 1 < row_num)
    matrix_has_up_cell = (i - 1 >= 0)
    matrix_has_right_cell = (j + 1 < col_num)
    matrix_has_left_cell = (j - 1 >= 0)

    opt_val_down = 0
    opt_val_up = 0
    opt_val_left = 0
    opt_val_right = 0

    if (matrix_has_down_cell and matrix[i][j] > matrix[i+1][j]):
        opt_val_down = OPT[i+1][j]
    if(matrix_has_up_cell and matrix[i][j] > matrix[i-1][j]):
        opt_val_up = OPT[i-1][j]
    if(matrix_has_right_cell and matrix[i][j] > matrix[i][j+1]):
        opt_val_right = OPT[i][j+1]
    if(matrix_has_left_cell and matrix[i][j] > matrix[i][j-1]):
        opt_val_left = OPT[i][j-1]

    return max(opt_val_down, opt_val_up, opt_val_left, opt_val_right)


def find_max_flow_length(matrix, row, column):
    cell_list = []
    for i in range(row):
        for j in range(column):
            cell_list.append((matrix[i][j], i, j))

    cell_list.sort()

    OPT = [[0] * column for row in range(row)]

    for val, i, j in cell_list:
        OPT[i][j] = find_max_opt_neighbor(matrix, OPT, i, j) + 1

    return max(max(row) for row in OPT)

def main():
    filename = sys.argv[1]
    contents = read_file(filename)
    row, column, matrix = ParseContent(contents)


    maxFlowLength = find_max_flow_length(matrix, row, column)
    print(maxFlowLength)
    #print(row, " " , column, "\n")
    #print_matrix(matrix)


if __name__ == "__main__":
    main()