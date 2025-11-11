#include <iostream>
using namespace std;

int main()
{
    int n = -128;
    char m = n;

    while (m == n)
    {
        cout << m << "  :  " << n << endl;
        n += 1;
        m = n;
    }
}