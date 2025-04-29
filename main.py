# Numerical Analysis - Solving Linear Systems using Jacobi and Gauss-Seidel Methods

MAX_ITERATIONS = 1000
TOLERANCE = 0.00001

# Define the system of equations
matrixA = [
    [4, 2, 0],
    [2, 10, 4],
    [0, 4, 5]
]

vectorB = [[2], [6], [5]]

# Validate input matrix and vector
if not matrixA or not all(isinstance(row, list) and row for row in matrixA):
    print("Error: The matrixA is empty or not properly formatted.")
    exit()

if len(matrixA) != len(vectorB):
    print("Error: Matrix and vector sizes do not match.")
    exit()

# Initialize guess
initial_guess = [0 for _ in range(len(vectorB))]

# Function to check if the matrix is diagonally dominant
def is_dominant_diagonal(matrix):
    for i in range(len(matrix)):
        if abs(matrix[i][i]) < sum(abs(matrix[i][j]) for j in range(len(matrix)) if i != j):
            return False
    return True

# Attempt to rearrange matrix to make it diagonally dominant
def attempt_fix_dominant_diagonal(matrix, vector):
    size = len(matrix)
    assigned_cols = [-1]*size
    new_matrix = [None]*size
    new_vector = [0]*size

    for i in range(size):
        for j in range(size):
            if abs(matrix[i][j]) >= sum(abs(matrix[i][k]) for k in range(size) if k != j):
                if assigned_cols.count(j) == 0:
                    assigned_cols[i] = j
                    break

    if -1 in assigned_cols:
        print("Could not rearrange the matrix to be diagonally dominant.")
        return matrix, vector

    for i in range(size):
        new_matrix[assigned_cols[i]] = matrix[i]
        new_vector[assigned_cols[i]] = vector[i]

    return new_matrix, new_vector

# Jacobi Method
def jacobi_method(matrix, vector, tolerance, max_iterations):
    size = len(matrix)
    x_old = [0.0 for _ in range(size)]
    x_new = x_old.copy()

    for iteration in range(1, max_iterations + 1):
        for i in range(size):
            if matrix[i][i] == 0:
                print(f"Cannot divide by zero at row {i}.")
                return
            sum_other = sum(matrix[i][j] * x_old[j] for j in range(size) if j != i)
            x_new[i] = (vector[i][0] - sum_other) / matrix[i][i]

        print(f"Iteration {iteration}: {x_new}")

        if all(abs(x_new[i] - x_old[i]) < tolerance for i in range(size)):
            print(f"Converged successfully in {iteration} iterations.")
            return

        x_old = x_new.copy()

    print("Jacobi method did not converge within the maximum number of iterations.")

# Gauss-Seidel Method
def gauss_seidel_method(matrix, vector, tolerance, max_iterations):
    size = len(matrix)
    x = [0.0 for _ in range(size)]

    for iteration in range(1, max_iterations + 1):
        x_old = x.copy()

        for i in range(size):
            if matrix[i][i] == 0:
                print(f"Cannot divide by zero at row {i}.")
                return
            sum_other = sum(matrix[i][j] * x[j] for j in range(size) if j != i)
            x[i] = (vector[i][0] - sum_other) / matrix[i][i]

        print(f"Iteration {iteration}: {x}")

        if all(abs(x[i] - x_old[i]) < tolerance for i in range(size)):
            print(f"Converged successfully in {iteration} iterations.")
            return

    print("Gauss-Seidel method did not converge within the maximum number of iterations.")

# Main Program
print("Solving Linear Systems using Iterative Methods\n")

if not is_dominant_diagonal(matrixA):
    print("Matrix is not diagonally dominant. Attempting to rearrange...")
    matrixA, vectorB = attempt_fix_dominant_diagonal(matrixA, vectorB)
    if not is_dominant_diagonal(matrixA):
        print("Warning: Matrix is still not diagonally dominant. Convergence is not guaranteed.")

try:
    method = int(input("Choose method:\n1 - Jacobi Method\n2 - Gauss-Seidel Method\nEnter your choice: "))
except ValueError:
    print("Invalid input. Please enter 1 or 2.")
    exit()

if method == 1:
    print("\nUsing Jacobi Method:\n")
    jacobi_method(matrixA, vectorB, TOLERANCE, MAX_ITERATIONS)
elif method == 2:
    print("\nUsing Gauss-Seidel Method:\n")
    gauss_seidel_method(matrixA, vectorB, TOLERANCE, MAX_ITERATIONS)
else:
    print("Invalid choice. Please enter either 1 or 2.")
