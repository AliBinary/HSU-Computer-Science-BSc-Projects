import sympy as sp


def calculate_q_b(f, variables):
    """
    Q matrix (Hessian) and b vector (gradient) for a quadratic function.

    Parameters:
    - f: The quadratic function (symbolic expression).
    - variables: List of symbolic variables (sympy symbols).

    Returns:
    - Q: The Hessian matrix (second derivative of the function).
    - b: The gradient vector (first derivative of the function).
    """
    # Calculate the gradient (first derivative)
    gradient = [sp.diff(f, var) for var in variables]

    # Calculate the Hessian (second derivative)
    hessian = [[sp.diff(gradient[i], var2) for var2 in variables]
               for i in range(len(variables))]

    # Extract Q (Hessian matrix) and b (gradient vector)
    Q = sp.Matrix(hessian)
    b = sp.Matrix(gradient)

    return Q, b


def get_user_input():
    """
    Get user input for the number of variables and the quadratic function.

    Returns:
    - f: The quadratic function as a sympy expression.
    - variables: List of symbolic variables.
    """
    # Get the number of variables
    num_vars = int(input("Enter the number of variables: "))

    # Get the variable names
    variables = [input(f"Enter name of variable {
                       i+1}: ") for i in range(num_vars)]

    # Define symbols for variables
    symbols = sp.symbols(variables)

    # Get the quadratic function from the user
    func_str = input(f"Enter the quadratic function in terms of {
                     ', '.join(variables)}: ")
    func = sp.sympify(func_str)  # Convert string input to sympy expression

    return func, symbols


def main():
    # Get user input for the quadratic function and variables
    f, variables = get_user_input()

    # Calculate Q and b
    Q, b = calculate_q_b(f, variables)

    # Display the results
    print("\nMatrix Q (Hessian):")
    sp.pprint(Q)  # Using pprint for better readability

    print("\nVector b (Gradient):")
    sp.pprint(b)  # Using pprint for better readability


if __name__ == "__main__":
    main()
