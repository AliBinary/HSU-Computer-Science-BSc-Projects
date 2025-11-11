#include <iostream>
using namespace std;

int mod(int a, int n, int m)
{
    if (n == 0)
        return 1;
    else if (n % 2 == 0)
    {
        int temp = mod(a, n / 2, m);
        return (temp * temp) % m;
    }
    else
    {
        int temp = mod(a, (n - 1) / 2, m);
        return (temp * temp * a) % m;
    }
}

int main()
{
    cout << mod(3, 10, 7);
    return 0;
}
