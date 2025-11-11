#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    cin >> n;
    int avg = 0, mini, maxi;

    for (int i = 0; i < n - 1; i++)
    {
        int x;
        cin >> x;
        avg += x;
        if (x > maxi)
            maxi = x;
        if (x < mini)
            mini = x;
    }
}