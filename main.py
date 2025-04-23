from methods import jacobi_method, gauss_seidel_method
from utils import is_diagonally_dominant

def main():
    print(" Start! The code has started running")

    # הגדרת המטריצה והוקטור
    matrixA = [[4, 2, 0], [2, 10, 4], [0, 4, 5]]
    vectorB = [[2], [6], [5]]

    # הדפסת מערכת המשוואות
    print("📘 The system of equations has been defined.")
    for row in matrixA:
        print(row)
    print("📘 vector B:", vectorB)

    # קלט מהמשתמש – איזו שיטה לבחור
    print("🔢 Choose a method (jacobi / gauss):")
    method = input(">> ").strip().lower()

    if method == "jacobi":
        print("\n Solution using the Jacobi method:")
        jacobi_method(matrixA, vectorB)
    elif method == "gauss":
        print("\n Solution using the Gauss-Seidel method:")
        gauss_seidel_method(matrixA, vectorB)
    else:
        print("Unrecognized method, try again.")

if __name__== "__main__":
    main()
