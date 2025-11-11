#include <bits/stdc++.h>
using namespace std;

void solidSquare(int n)
{
    int i, j;
    for (i = 1; i <= n; i++)
    {
        for (j = 1; j <= n; j++)
            cout << "*";
        cout << "\n";
    }
}

int main()
{
    int rows = 3;
    solidSquare(rows);
    return 0;
}