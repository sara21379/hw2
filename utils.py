from itertools import permutations

def is_diagonally_dominant(matrix):
    """
    Checks if a matrix is diagonally dominant.
    A matrix is diagonally dominant if for every row,
    the absolute value of the diagonal element is greater than 
    or equal to the sum of the absolute values of the other elements in that row.
    """
    for i in range(len(matrix)):
        diag = abs(matrix[i][i])
        row_sum = sum(abs(matrix[i][j]) for j in range(len(matrix)) if j != i)
        if diag < row_sum:
            return False
    return True


def make_diagonally_dominant(matrix, vector):
    """
    Attempts to reorder the rows of the matrix and the corresponding vector
    to form a diagonally dominant matrix.

    Returns:
        (new_matrix, new_vector) if a valid arrangement is found,
        (None, None) otherwise.
    """
    n = len(matrix)
    for perm in permutations(range(n)):
        new_matrix = [matrix[i] for i in perm]
        new_vector = [vector[i] for i in perm]
        if is_diagonally_dominant(new_matrix):
            return new_matrix, new_vector, True
    return matrix, vector, False

def to_diagonally_dominant(matrix, vector):
    if not is_diagonally_dominant(matrix):
        matrix, vector, success = make_diagonally_dominant(matrix, vector)
        if not success:
            print("⚠ The matrix is not diagonally dominant and cannot be rearranged. Proceeding anyway...")
            matrix = [[float(val) for val in row] for row in matrix]
        else:
            print("✅ The matrix was rearranged to be diagonally dominant.")
    return matrix, vector