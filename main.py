from itertools import permutations

MAX_ITERATIONS = 1000
TOLERANCE = 0.00001

# Define the system of equations
matrixA = [
    [4, 2, 0],
    [2, 10, 4],
    [0, 4, 5]
]

vectorB = [[2], [6], [5]]

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
            print("The matrix is not diagonally dominant and cannot be rearranged. Proceeding anyway...")
        else:
            print("The matrix was rearranged to be diagonally dominant.")
    matrix = [[float(val) for val in row] for row in matrix]
    vector = [[float(val[0])] for val in vector]
    return matrix, vector


def jacobi_method(matrix, vector, TOLERANCE, MAX_ITERATIONS):
    """
    Solves a system of linear equations using the Jacobi iterative method.
    """
    try:
        n = len(matrix)
        x = [0 for _ in range(n)]
        x_new = x[:]

        # Make sure it is diagonal dominance
        matrix, vector = to_diagonally_dominant(matrix, vector)

        for iteration in range(1, MAX_ITERATIONS + 1):
            for i in range(n):
                s = sum(matrix[i][j] * x[j] for j in range(n) if j != i)
                x_new[i] = (vector[i][0] - s) / matrix[i][i]

            print(f"Iteration {iteration}: {x_new}")

            # Convergence check
            diff = [abs(x_new[i] - x[i]) for i in range(n)]
            if max(diff) < TOLERANCE:
                print(f"\nSolution converged after {iteration} iterations.")
                return x_new

            x = x_new[:]

        return None

    except ZeroDivisionError as e:
        print(f"Error occurred!\n{e}")
        return None

    except ValueError as e:
        print(f"Error occurred!\n{e}")
        return None

    except Exception as e:
        print(f"Error occurred!\n{e}")
        return  None

def gauss_seidel_method(matrix, vector, TOLERANCE, MAX_ITERATIONS):
    """
    Solves a system of linear equations using the Gauss-Seidel iterative method.
    """
    try:
        n = len(matrix)
        x = [0 for _ in range(n)]

        # Make sure it is diagonal dominance
        matrix, vector = to_diagonally_dominant(matrix, vector)

        for iteration in range(1, MAX_ITERATIONS + 1):
            x_old = x.copy()
            for i in range(n):
                s = sum(matrix[i][j] * x[j] for j in range(n) if j != i)
                x[i] = (vector[i][0] - s) / matrix[i][i]

            print(f"Iteration {iteration}: {x}")

            # Convergence check
            diff = [abs(x[i] - x_old[i]) for i in range(n)]
            if max(diff) < TOLERANCE:
                print(f"\nSolution converged after {iteration} iterations.")
                return x

        return None

    except ZeroDivisionError as e:
        print(f"Error occurred!\n{e}")
        return None

    except ValueError as e:
        print(f"Error occurred!\n{e}")
        return None

    except Exception as e:
        print(f"Error occurred!\n{e}")
        return  None


def main():
    print(" Start! The code has started running")
    try:

        # הדפסת מערכת המשוואות
        print("The system of equations has been defined.")
        for row in matrixA:
            print(row)
        print("vector B:", vectorB)

        try:
            method = int(input("Choose method:\n1 - Jacobi Method\n2 - Gauss-Seidel Method\nEnter your choice: "))
        except ValueError:
            print("Invalid input. Please enter 1 or 2.")
            exit()

        if method == 1:
            print("\nUsing Jacobi Method:\n")
            solution = jacobi_method(matrixA, vectorB, TOLERANCE, MAX_ITERATIONS)
        elif method == 2:
            print("\nUsing Gauss-Seidel Method:\n")
            solution = gauss_seidel_method(matrixA, vectorB, TOLERANCE, MAX_ITERATIONS)
        else:
            raise ValueError()

        if solution:
            print(f"\nFinal solution: {solution}")
        else:
            print("The method did not converge.")

    except ValueError:
        print("Invalid input. Please enter 1 or 2.")

    except Exception as e:
        print("\nAn unexpected error occurred.")
        print(e)

if __name__== "__main__":
    main()
