from utils import to_diagonally_dominant

def jacobi_method(matrix, vector, epsilon=0.00001, max_iterations=100):
    """
    Solves a system of linear equations using the Jacobi iterative method.
    """
    try:
        n = len(matrix)
        x = [0 for _ in range(n)]
        x_new = x[:]

        # Make sure it is diagonal dominance
        matrix, vector = to_diagonally_dominant(matrix, vector)

        for iteration in range(1, max_iterations + 1):
            for i in range(n):
                s = sum(matrix[i][j] * x[j] for j in range(n) if j != i)
                x_new[i] = (vector[i][0] - s) / matrix[i][i]

            print(f"Iteration {iteration}: {x_new}")

            # Convergence check
            diff = [abs(x_new[i] - x[i]) for i in range(n)]
            if max(diff) < epsilon:
                print(f"\n✅ Solution converged after {iteration} iterations.")
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

def gauss_seidel_method(matrix, vector, epsilon=0.00001, max_iterations=100):
    """
    Solves a system of linear equations using the Gauss-Seidel iterative method.
    """
    try:
        n = len(matrix)
        x = [0 for _ in range(n)]

        # Make sure it is diagonal dominance
        matrix, vector = to_diagonally_dominant(matrix, vector)

        for iteration in range(1, max_iterations + 1):
            x_old = x.copy()
            for i in range(n):
                s = sum(matrix[i][j] * x[j] for j in range(n) if j != i)
                x[i] = (vector[i][0] - s) / matrix[i][i]

            print(f"Iteration {iteration}: {x}")

            # Convergence check
            diff = [abs(x[i] - x_old[i]) for i in range(n)]
            if max(diff) < epsilon:
                print(f"\n✅ Solution converged after {iteration} iterations.")
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