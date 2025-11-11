/*
    author:  AliBinary
    Email: AliGhanbariCs@gmail.com
    GitHub: https://github.com/AliBinary
    created: 21.06.2024 14:53:10
*/

#include <bits/stdc++.h>
#include <windows.h>
using namespace std;

int main()
{
    cout << "welcome." << endl;
    cout << "Size of Matrix: ";
    int N, M;
    cin >> N >> M;
    vector<vector<float>> matrix(N, vector<float>(M, -1));
    cout << "\nenter elements row by row: \n";
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            cin >> matrix[i][j];
        }
    }

    // Sleep(1000);
    cout << endl
         << "Your matrix was this: " << endl;

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            cout << matrix[i][j] << ' ';
        }
        cout << endl;
    }

    cout << endl;

    for (int i = 0; i < min(N, M - 1); i++)
    {
        bool flag = true;
        if (matrix[i][i] == 0)
        {
            flag = false;
            for (int j = i + 1; j < N; j++)
            {
                if (matrix[j][i] != 0)
                {
                    for (int q = 0; q < M; q++)
                    {
                        swap(matrix[i][q], matrix[j][q]);
                    }
                    flag = true;
                }
            }
        }
        if (flag)
        {
            for (int j = 0; j < M; j++)
            {
                if (j == i)
                    continue;
                matrix[i][j] /= matrix[i][i];
            }
            matrix[i][i] = 1;
            for (int k = i + 1; k < N; k++)
            {
                bool zaribeshe = true;
                for (int j = i + 1; j < M; j++)
                {
                    if (matrix[k][j] / matrix[k][i] != matrix[i][j])
                    {
                        zaribeshe = false;
                        break;
                    }
                }
                if (zaribeshe)
                {
                    for (int j = i + 1; j < M; j++)
                    {
                        matrix[k][j] = 0;
                    }
                }
                else
                    for (int j = i + 1; j < M; j++)
                    {
                        matrix[k][j] += (-1) * (matrix[i][i]) * (matrix[k][i]);
                    }
                matrix[k][i] = 0;
            }
        }
    }

    cout << endl
         << "Now the matrix after performing the Gauss-Jordan algorithm is this: " << endl;
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            cout << matrix[i][j] << ' ';
        }
        cout << endl;
    }
}