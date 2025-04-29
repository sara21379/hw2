from methods import jacobi_method, gauss_seidel_method
from utils import is_diagonally_dominant

def main():
    print(" Start! The code has started running")

    # הגדרת המטריצה והוקטור
    matrix = [[4, 2, 0], [2, 10, 4], [0, 4, 5]]
    vector = [[2], [6], [5]]

    # הדפסת מערכת המשוואות
    print("📘 The system of equations has been defined.")
    for row in matrix:
        print(row)
    print("📘 vector B:", vector)

    # קלט מהמשתמש – איזו שיטה לבחור
    method = input("🔢 Choose a method (jacobi / gauss):\n>> ").strip().lower()

    if method == "jacobi":
        print("\n Solution using the Jacobi method:")
        solution = jacobi_method(matrix, vector)
    elif method == "gauss":
        print("\n Solution using the Gauss-Seidel method:")
        solution = gauss_seidel_method(matrix, vector)
    else:
        solution = None
        print("Unrecognized method, try again.")

    if solution:
        print(f"\n✅ Final solution: {solution}")
    else:
        print("❌ The method did not converge.")

if __name__== "__main__":
    main()
