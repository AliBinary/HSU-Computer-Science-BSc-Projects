#include <bits/stdc++.h>
using namespace std;

bool isprime(int x)
{
    for (int i = 2; i <= sqrt(x); i++)
    {
        if (x % i)
            continue;
        return false;
    }
    return true;
}

int main()
{
    int num;
    cin >> num;

    cout << num;
    if (!isprime(num))
        cout << " not";
    cout << " prime!";
}