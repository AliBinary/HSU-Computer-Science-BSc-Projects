#include <bits/stdc++.h>
using namespace std;

int fact(int x)
{
    int ans = 1;
    for (int i = 2; i <= x; i++)
    {
        ans *= i;
    }
    return x;
}

int main()
{
    int x;
    cin >> x;
    cout << fact(x);
}