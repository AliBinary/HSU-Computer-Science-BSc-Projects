#include <bits/stdc++.h>
using namespace std;

int max(int, int);
int main()
{
    int m, n;
    do
    {
        cin >> m >> n;
        cout << "max(" << m << "," << n << ")=";
        cout << max(m, n) << endl;
    } while (m != 0 && n != 0);
}
int max(int x, int y)
{
    return (x > y) ? x : y;
}