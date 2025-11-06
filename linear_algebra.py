tester = [[0, 0, 3], 
          [4, 0, 2], 
          [7, 4, 1]]

def determinant_2x2(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]

def determinant_3x3(matrix):
    output = 0
    indexer = {
        0: [1, 1, 2, 2, 2, 1, 1, 2], 
        1: [0, -1, 1, 1, 1, -1, 0, 1],
        2: [-1, -2, 0, -1, 0, -2, -1, -1]
    }
    sign = -1
    for n in range(3):
        sign *= -1
        values = indexer[n]
        first = matrix[n+values[0]][n+values[1]]
        second = matrix[n+values[2]][n+values[3]]
        third = matrix[n+values[4]][n+values[5]]
        fourth = matrix[n+values[6]][n+values[7]]
        output += (sign * matrix[0][n] * ((first * second) - (third * fourth)))
    
    return output

def get_rref_3x3(matrix, display_steps):
    '''
    pass in a 3x3 square matrix
    will return the matrix in RREF
    will also display steps if you want
    '''

    if not display_steps:
        diagonal_indexes = []
        zero_at_pivot = []

        for i in range(3):
            if matrix[i][i] == 0:
                # if anything gets added here, it means there is a problem
                # the problem can possibly be solved by exchanging rows
                # 
                zero_at_pivot.append((i, i))
            diagonal_indexes.append((i, i))
        print(zero_at_pivot)
        print(diagonal_indexes)

        # checking to see if any rows contain all zeros
        # also if it would be a good idea to change row orders
        for i, row in enumerate(matrix):
            if 0 in row:
                pass

        got_pivot = False

        pivot_position = (0, 0)
        while not got_pivot:
            for i, row in enumerate(matrix):
                for j, element in enumerate(row):
                    if element != 0: 
                        pivot_position = (i, j)
                        got_pivot = True
                        break
                if got_pivot:
                    break

