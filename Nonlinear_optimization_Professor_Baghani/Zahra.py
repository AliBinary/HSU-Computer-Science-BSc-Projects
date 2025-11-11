import sympy as sp


def get_user_input():

    # Get the number of variables
    num_vars = int(input("\nEnter the number of variables: "))

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


def extract_q_b(f, variables):

    # Calculate the Hessian (second derivatives)
    hessian = [[sp.diff(f, var1, var2) for var2 in variables]
               for var1 in variables]
    Q = sp.Matrix(hessian)

    # Extract numeric coefficients of linear terms
    b = sp.Matrix([
        sp.diff(f, var).subs({v: 0 for v in variables}) for var in variables
    ])

    # Calculate the gradient (first derivative)
    gradient = [sp.diff(f, var) for var in variables]
    c = sp.Matrix(gradient)

    return Q, b, c


def find_critical_points(f, variables):
    # Solve ∇f = 0 to find critical points
    gradient = [sp.diff(f, var) for var in variables]
    critical_points = sp.solve(gradient, variables, dict=True)
    return critical_points


def classify_critical_points(Q, critical_points, variables):
    classifications = []
    for point in critical_points:
        # Handle both dict and list outputs from solve
        substitutions = {var: point[var] for var in variables} if isinstance(
            point, dict) else dict(zip(variables, point))

        # Substitute the critical point into the Hessian matrix
        Q_at_point = Q.subs(substitutions)

        # Determine the definiteness of the Hessian
        eigenvalues = Q_at_point.eigenvals()
        eigenvalues = [sp.re(ev.evalf())
                       for ev in eigenvalues]  # Ensure numeric values

        if all(val > 0 for val in eigenvalues):  # All eigenvalues positive
            classifications.append((substitutions, "Local Minimum"))
        elif all(val < 0 for val in eigenvalues):  # All eigenvalues negative
            classifications.append((substitutions, "Local Maximum"))
        else:  # Mixed signs
            classifications.append((substitutions, "Saddle Point"))
    return classifications


def main():
    # Get user input for the quadratic function and variables
    f, variables = get_user_input()

    # Extract Q and b
    Q, linear_coeffs, gradiant = extract_q_b(f, variables)

    # Find critical points
    critical_points = find_critical_points(f, variables)

    # Classify critical points
    classifications = classify_critical_points(Q, critical_points, variables)

    # Display the results
    print("\nMatrix Q (Hessian):")
    sp.pprint(Q)  # Display Hessian matrix (Q)

    print("\nVector b (Numeric linear coefficients):")
    sp.pprint(linear_coeffs)  # Display numeric linear coefficients vector (b)

    print("\nVector c (Gradient):")
    sp.pprint(gradiant)

    print("\nCritical Points and Classification:")
    for point, classification in classifications:
        print(f"Point: {point}, Classification: {classification}\n")


if __name__ == "__main__":
    main()
