#include <iostream>
using namespace std;

int main()
{
    int q;
    cin >> q;
    const int N = q;
    unsigned long long int fibs[N] = {};

    fibs[0] = 0;
    fibs[1] = 1;
    cout << endl;
    for (int i = 2; i <= N; i++)
    {
        fibs[i] = fibs[i - 1] + fibs[i - 2];
    }

    for (int i = 0; i <= N; i++)
    {
        cout << fibs[i] << endl;
    }
}