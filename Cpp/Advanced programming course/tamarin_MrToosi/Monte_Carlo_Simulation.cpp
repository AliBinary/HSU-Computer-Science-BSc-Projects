#include <bits/stdc++.h>
using namespace std;

int main()
{
    int x, y, n, ok = 0;
    // cout << "Note! your rand_max is : " << RAND_MAX << endl;
    cout << "please enter the number for do simulation: ";
    cin >> n;
    srand(time(0));

    cout << fixed;

    for (int i = 1; i <= n; i++)
    {
        x = rand() % 20001 - 10000;
        y = rand() % 20001 - 10000;
        if (x * x + y * y <= 10000 * 10000)
            ok++;
    }
    float pi = ((float)ok / n) * 4;
    cout << pi;

    return 0;
}