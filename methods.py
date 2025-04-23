from utils import is_diagonally_dominant, make_diagonally_dominant

def jacobi_method(A, b, epsilon=0.00001, max_iterations=100):
    """
    Solves a system of linear equations using the Jacobi iterative method.
    """
    n = len(A)
    x = [0 for _ in range(n)]  # Initial guess vector
    x_new = x[:]

    # Check diagonal dominance
    if not is_diagonally_dominant(A):
        A, b = make_diagonally_dominant(A, b)
        if A is None:
            print("⚠ The matrix is not diagonally dominant and cannot be rearranged. Proceeding anyway...")
            A = [[float(val) for val in row] for row in A]
        else:
            print("✅ The matrix was rearranged to be diagonally dominant.")

    for iteration in range(1, max_iterations + 1):
        for i in range(n):
            s = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i][0] - s) / A[i][i]

        print(f"Iteration {iteration}: {x_new}")

        # Convergence check
        diff = [abs(x_new[i] - x[i]) for i in range(n)]
        if max(diff) < epsilon:
            print(f"\n✅ Solution converged after {iteration} iterations.")
            print(f"🔹 Final solution: {x_new}")
            return x_new

        x = x_new[:]

    print("\n❌ The system did not converge within the maximum number of iterations.")
    return None


def gauss_seidel_method(A, b, epsilon=0.00001, max_iterations=100):
    """
    Solves a system of linear equations using the Gauss-Seidel iterative method.
    """
    n = len(A)
    x = [0 for _ in range(n)]

    # Check diagonal dominance
    if not is_diagonally_dominant(A):
        A, b = make_diagonally_dominant(A, b)
        if A is None:
            print("⚠ The matrix is not diagonally dominant and cannot be rearranged. Proceeding anyway...")
            A = [[float(val) for val in row] for row in A]
        else:
            print("✅ The matrix was rearranged to be diagonally dominant.")

    for iteration in range(1, max_iterations + 1):
        x_old = x.copy()
        for i in range(n):
            s = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x[i] = (b[i][0] - s) / A[i][i]

        print(f"Iteration {iteration}: {x}")

        # Convergence check
        diff = [abs(x[i] - x_old[i]) for i in range(n)]
        if max(diff) < epsilon:
            print(f"\n✅ Solution converged after {iteration} iterations.")
            print(f"🔹 Final solution: {x}")
            return x

    print("\n❌ The system did not converge within the maximum number of iterations.")
    return None