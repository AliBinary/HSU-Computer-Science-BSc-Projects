#include <bits/stdc++.h>
using namespace std;

int pow(int x, int y)
{
    long p = 1;
    for (int i = 1; i <= y; i++)
    {
        p *= x;
    }
}
int main()
{
    int x, y;
    cin >> x >> y;
    cout << pow(x, y);
}