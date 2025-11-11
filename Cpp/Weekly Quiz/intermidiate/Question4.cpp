#include <iostream>
using namespace std;

int main()
{
    int row, col;

    cout << "Enter the number of rows of the matrix: ";
    cin >> row;
    cout << "Enter the number of matrix columns: ";
    cin >> col;

    int matrix[row][col];

    for (int i = 0; i < row; i++)
    {
        cout << "\nOK, enter the numbers of row number " << i + 1 << " of the matrix: ";
        for (int j = 0; j < col; j++)
        {
            cin >> matrix[i][j];
        }
    }

    int n, m, num, flag = 0;
    for (int i = 0; !flag && i < row; i++)
    {
        for (int j = 0; !flag && j < col; j++)
        {
            flag = 1;
            for (int I = 0; I < row; I++)
            {
                if (matrix[I][j] > matrix[i][j])
                {
                    flag = 0;
                    break;
                }
            }

            if (flag)
                for (int J = 0; J < col; J++)
                {
                    if (matrix[i][J] < matrix[i][j])
                    {
                        flag = 0;
                        break;
                    }
                }

            if (flag)
            {
                n = i;
                m = j;
                num = matrix[i][j];
            }
        }
    }

    if (flag)
        cout << "\nThis matrix has a horse saddle point!\n"
             << " it's number : " << num
             << ", in the row : " << n + 1
             << " ans in the column : " << m + 1 << endl;
    else
        cout << "\nThis matrix has not a horse saddle point!\n";
}