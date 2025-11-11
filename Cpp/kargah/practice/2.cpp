#include <bits/stdc++.h>
using namespace std;

int gcd(int a, int b)
{
    int ans = 1;
    for (int i = min(a, b); i >= 1; i--)
    {
        if (a % i == 0 && b % i == 0)
        {
            ans = i;
            break;
        }
    }
    return ans;
}

int main()
{
    int a, b;
    cin >> a >> b;
    cout << gcd(a, b);
}