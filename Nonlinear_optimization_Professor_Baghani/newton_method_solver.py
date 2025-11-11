import sympy as sp
import numpy as np


def get_user_input():
    """
    Get user input for the number of variables, equations, and initial guesses.
    Returns the system of equations and the Jacobian matrix.
    """
    # Get the number of variables
    num_vars = int(input("Enter the number of variables: "))

    # Get the variable names
    variables = [input(f"Enter name of variable {
                       i+1}: ") for i in range(num_vars)]

    # Define symbols for variables
    symbols = sp.symbols(variables)

    # Get the number of equations
    num_eqns = int(input("Enter the number of equations: "))

    # Get the equations from the user
    equations = []
    for i in range(num_eqns):
        eqn = input(f"Enter equation {
                    i+1} in terms of {', '.join(variables)}: ")
        # Convert string input to sympy expression
        equations.append(sp.sympify(eqn))

    # Create lambdified functions
    F_func = [sp.lambdify(symbols, eqn) for eqn in equations]

    # Compute the Jacobian matrix (derivatives of each equation with respect to each variable)
    J_func = np.array([[sp.lambdify(symbols, sp.diff(eqn, var))
                      for var in symbols] for eqn in equations])

    # Get initial guesses for the solution
    x0 = np.array(
        [float(input(f"Enter initial guess for {var}: ")) for var in variables])

    return F_func, J_func, x0


def newton_method(F, J, x0, tol=1e-6, max_iter=100):
    """
    Solve a system of nonlinear equations using Newton's method.

    Parameters:
    - F: List of functions representing the system of equations
    - J: Jacobian matrix (list of partial derivatives)
    - x0: Initial guess for the solution (array or list)
    - tol: Tolerance for convergence (default 1e-6)
    - max_iter: Maximum number of iterations (default 100)

    Returns:
    - solution: The solution to the system of equations
    """
    # Convert initial guess to numpy array for easier manipulation
    x = np.array(x0, dtype=np.float64)
    for _ in range(max_iter):
        # Calculate F(x) and J(x)
        # Evaluate functions at current x
        F_val = np.array([f(*x) for f in F], dtype=np.float64)
        J_val = np.array([[j(*x) for j in row]
                         for row in J], dtype=np.float64)  # Evaluate Jacobian

        # Solve J(x) * delta = -F(x) for delta
        delta = np.linalg.solve(J_val, -F_val)

        # Update x
        x = x + delta

        # Check for convergence
        if np.linalg.norm(delta) < tol:
            print("Convergence reached.")
            return x

    print("Maximum iterations reached.")
    return x


def main():
    # Get user input for equations and initial guesses
    F_func, J_func, x0 = get_user_input()

    # Solve the system using Newton's method
    solution = newton_method(F_func, J_func, x0)

    # solution = newton_method(F_func, J_func, x0, 1e3, 10)

    # Display the solution
    print("Solution:", solution)


if __name__ == "__main__":
    main()


# Example:
# Solve the following system of nonlinear equations:
#   x^2-y^2=1
#   9*x^2+4*y^2=36
#
# Variables:
#   x
#   y
#
# Equations:
#   x^2 -y^2 -1 = 0
#   9*x^2 +4*y^2 -36 = 0
#
# Initial guesses:
#   x_0 = 1.5
#   y_0 = 2.5
