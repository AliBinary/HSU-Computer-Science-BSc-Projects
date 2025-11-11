#include <bits/stdc++.h>
using namespace std;

void hollowSquare(int rows)
{
    int i, j;
    for (i = 1; i <= rows; i++)
    {
        if (i == 1 || i == rows)
            for (j = 1; j <= rows; j++)
                cout << "*";

        else
            for (j = 1; j <= rows; j++)
                if (j == 1 || j == rows)
                    cout << "*";
                else
                    cout << " ";
        cout << "\n";
    }
}
int main()
{
    int rows;
    cout << "enter rows: ";
    cin >> rows;
    cout << "\nHollow Square:\n";

    hollowSquare(rows);
    return 0;
}
