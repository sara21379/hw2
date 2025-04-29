# Iterative Solver - Jacobi & Gauss-Seidel

This project implements an iterative method for solving a system of linear equations.  
Two numerical methods are included:
- Jacobi Method
- Gauss-Seidel Method

The system is hardcoded into the program, and the user can choose which method to apply.  
The program checks for diagonal dominance and attempts to rearrange the matrix if needed.  
All iterations are printed until the stopping condition is reached (epsilon = 0.00001).

The system includes input validation for matrix structure, dimension matching, division by zero, and diagonal dominance.  
In case of any error, a clear and informative message is displayed.  
Users are notified of invalid input or lack of convergence after the maximum number of iterations.  
These checks ensure the stability and accuracy of the solution process.
