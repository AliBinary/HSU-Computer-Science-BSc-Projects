#include <iostream>
using namespace std;

int main()
{
    int n, d;
    cin >> n >> d;
    if (n % d)
        cout << n << " is not  divisible by " << d;
    else
        cout << n << " is  divisble by " << d;
}