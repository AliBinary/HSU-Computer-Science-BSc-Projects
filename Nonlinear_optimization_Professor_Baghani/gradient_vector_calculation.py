import sympy as sp


def calculate_gradient(f, variables):
    """
    Calculate the gradient of a function with respect to a list of variables.

    Parameters:
    - f: The function for which the gradient is calculated.
    - variables: A list of symbolic variables (sympy symbols).

    Returns:
    - gradient: A list of partial derivatives of the function with respect to each variable.
    """
    gradient = [sp.diff(f, var)
                for var in variables]  # Calculate partial derivatives
    return gradient


def get_user_input():
    """
    Get user input for the number of variables, variable names, and the function.

    Returns:
    - f: The function as a sympy expression.
    - variables: List of symbolic variables.
    """
    # Get the number of variables
    num_vars = int(input("Enter the number of variables: "))

    # Get the variable names
    variables = [input(f"Enter name of variable {
                       i+1}: ") for i in range(num_vars)]

    # Define symbols for variables
    symbols = sp.symbols(variables)

    # Get the function from the user
    func_str = input(f"Enter the function in terms of {
                     ', '.join(variables)}: ")
    func = sp.sympify(func_str)  # Convert string input to sympy expression

    return func, symbols


def main():
    # Get user input for the function and variables
    f, variables = get_user_input()

    # Calculate the gradient
    gradient = calculate_gradient(f, variables)

    # Display partial derivatives (individual derivatives)
    print("\nPartial derivatives:")
    for i, partial_derivative in enumerate(gradient):
        print(f"∂f/∂{variables[i]} = {partial_derivative}")

    # Display the gradient vector
    print("\nGradient vector:", gradient)


if __name__ == "__main__":
    main()
