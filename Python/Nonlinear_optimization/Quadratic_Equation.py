def extract_q_b(coefficients):
    a, b, c, d, e, f = coefficients

    # Define matrix Q as a list of lists
    Q = [[2 * a, b],
         [b, 2 * c]]

    # Define vector b as a list
    b_vector = [d, e]

    return Q, b_vector


# Example coefficients for f(x, y) = 2x^2 + 3xy + y^2 + 4x + 5y + 6
coefficients = (2, 3, 1, 4, 5, 6)
Q, b = extract_q_b(coefficients)

print("Matrix Q:")
for row in Q:
    print(row)

print("Vector b:")
print(b)
