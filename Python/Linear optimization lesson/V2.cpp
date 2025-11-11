#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<double> get_vector(int size)
{
    vector<double> v(size);
    for (double &val : v)
    {
        cin >> val;
    }
    return v;
}

vector<vector<double>> get_matrix(int rows, int cols)
{
    vector<vector<double>> m(rows, vector<double>(cols));
    for (vector<double> &row : m)
    {
        for (double &val : row)
        {
            cin >> val;
        }
    }
    return m;
}

void print_tableau(vector<vector<double>> &tableau)
{
    for (auto &row : tableau)
    {
        for (auto &val : row)
        {
            cout << val << ' ';
        }
        cout << '\n';
    }
    cout << '\n';
}

vector<vector<double>> revised_simplex(vector<double> c, vector<vector<double>> A, vector<double> b)
{
    int num_vars = c.size();
    int num_constraints = b.size();

    // Initialize the tableau
    vector<vector<double>> tableau(num_constraints + 1, vector<double>(num_vars + num_constraints + 1));
    for (int i = 0; i < num_constraints; ++i)
    {
        for (int j = 0; j < num_vars; ++j)
        {
            tableau[i][j] = A[i][j];
        }
        tableau[i][num_vars + i] = 1;
        tableau[i][num_vars + num_constraints] = b[i];
    }
    for (int j = 0; j < num_vars; ++j)
    {
        tableau[num_constraints][j] = c[j];
    }

    print_tableau(tableau);

    // Main loop
    while (true)
    {
        int pivot_column = max_element(tableau[num_constraints].begin(), tableau[num_constraints].end()) - tableau[num_constraints].begin();
        if (tableau[num_constraints][pivot_column] <= 0)
            break;

        pair<double, int> min_ratio = {1e9, -1};
        for (int i = 0; i < num_constraints; ++i)
        {
            if (tableau[i][pivot_column] > 0 && tableau[i][num_vars + num_constraints] / tableau[i][pivot_column] < min_ratio.first)
            {
                min_ratio = {tableau[i][num_vars + num_constraints] / tableau[i][pivot_column], i};
            }
        }
        int pivot_row = min_ratio.second;

        double pivot_element = tableau[pivot_row][pivot_column];
        for (int j = 0; j <= num_vars + num_constraints; ++j)
        {
            tableau[pivot_row][j] /= pivot_element;
        }
        for (int i = 0; i <= num_constraints; ++i)
        {
            if (i != pivot_row)
            {
                double multiplier = tableau[i][pivot_column];
                for (int j = 0; j <= num_vars + num_constraints; ++j)
                {
                    tableau[i][j] -= multiplier * tableau[pivot_row][j];
                }
            }
        }

        print_tableau(tableau);
    }

    return tableau;
}

int main()
{
    int num_vars, num_constraints;
    cout << "Enter the number of variables: ";
    cin >> num_vars;
    cout << "Enter the number of constraints: ";
    cin >> num_constraints;

    cout << "Enter the coefficients of the objective function: ";
    vector<double> c = get_vector(num_vars);

    cout << "Enter the coefficients of the constraints: ";
    vector<vector<double>> A = get_matrix(num_constraints, num_vars);

    cout << "Enter the RHS values of the constraints: ";
    vector<double> b = get_vector(num_constraints);

    vector<vector<double>> tableau = revised_simplex(c, A, b);
    cout << "Optimal solution: " << tableau.back().back() << '\n';
    return 0;
}
