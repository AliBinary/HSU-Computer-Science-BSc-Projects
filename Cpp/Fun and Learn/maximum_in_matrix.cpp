#include <iostream>
using namespace std;

int main()
{
    int a[3][3];
    for (int i = 0; i < 3; i++)
        for (int j = 0; j < 3; j++)
            cin >> a[i][j];

    int k = a[0][0];
    for (int i = 0; i < 3; i++)
        for (int j = 0; j < 3; j++)
            if (a[i][j] > k)
                k = a[i][j];
    cout << k;
}