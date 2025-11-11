#include <iostream>
using namespace std;

int sum_with_sigma(int);
int sum_with_formula(int);

int main()
{
    int n = 105;
    sum_with_sigma(n);
    cout << endl;
    sum_with_formula(n);
}

int sum_with_sigma(int n)
{
    int sum = 0;
    for (int i = 0; i <= n; i++)
        sum += i;
    cout << sum;
}
int sum_with_formula(int n)
{
    int sum = n * (n + 1) / 2;
    cout << sum;
}