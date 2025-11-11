#include <iostream>
using namespace std;

int fact(int);
int comb(int, int);
int per(int, int);

int main()
{
    int n, r;
    cout << "enter n: ";
    cin >> n;
    cout << "enter r: ";
    cin >> r;

    cout << "\nPermutation: " << per(n, r) << endl;
    cout << "Combination: " << comb(n, r) << endl;
}

int fact(int n)
{
    if (n == 0 | n == 1)
        return 1;
    return n * fact(n - 1);
}

int comb(int n, int r)
{
    return fact(n) / (fact(r) * fact(n - r));
}

int per(int n, int r)
{
    return fact(n) / fact(n - r);
}