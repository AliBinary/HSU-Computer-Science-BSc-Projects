import numpy as np


def print_tableau(tableau, step):
    print(f"Step {step}:")
    print(tableau)
    print()


def revised_simplex(c, A, b):
    num_vars = len(c)
    num_constraints = len(b)

    # Initialize the tableau
    tableau = np.zeros((num_constraints + 1, num_vars + num_constraints + 1))
    tableau[:-1, :num_vars] = A
    tableau[:-1, num_vars:num_vars+num_constraints] = np.eye(num_constraints)
    tableau[:-1, -1] = b
    tableau[-1, :num_vars] = c
    tableau[-1, -1] = 0

    step = 0
    print_tableau(tableau, step)

    # Main loop
    while np.any(tableau[-1, :-1] > 0):
        pivot_column = np.argmax(tableau[-1, :-1])
        ratios = tableau[:-1, -1] / tableau[:-1, pivot_column]
        pivot_row = np.argmin(np.where(ratios > 0, ratios, np.inf))
        pivot_element = tableau[pivot_row, pivot_column]
        tableau[pivot_row, :] /= pivot_element
        for i in range(len(tableau)):
            if i != pivot_row:
                tableau[i, :] -= tableau[i, pivot_column] * \
                    tableau[pivot_row, :]
        step += 1
        print_tableau(tableau, step)
    return tableau


# Example usage:
# c = np.array([3, 2])
# A = np.array([[1, -1], [3, 1], [4, 3]])
# b = np.array([2, 5, 7])

# تعریف ضرایب تابع هدف
c = []

# تعریف ضرایب قیود نامساوی
A = [[1, -1], [3, 1], [4, 3]]

# تعریف سمت راست قیود نامساوی
b = [2, 5, 7]

tableau = revised_simplex(c, A, b)
print("Optimal solution:", tableau[-1, -1])
