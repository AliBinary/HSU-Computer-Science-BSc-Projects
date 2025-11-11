#include <bits/stdc++.h>
using namespace std;

int main()
{
    int x, y;
    cin >> x >> y;
    int ans = 1;
    if (y < 0)
    {
        y *= -1;
        for (int i = 0; i < y; i++)
        {
            ans *= x;
        }
    }
    else
    {
        for (int i = 0; i < y; i++)
        {
            ans *= x;
        }
    }
}