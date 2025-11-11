#include <iostream>
#include <math.h>
using namespace std;

int factorial(int n)
{
    if (n < 2)
        return 1;
    return (n * factorial(n - 1));
}

int main()
{
    unsigned long long int num = factorial(26) / 365;
    long int year = 1000 * 3600 * 12;
    cout << "we need " << num / year << " years to check all of them!";
}