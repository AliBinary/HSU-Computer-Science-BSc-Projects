#include <iostream>
using namespace std;

int main()
{
    int x, y;
    cin >> x >> y;
    if (abs(x * 1. / y - 1.618) < 0.1)
        cout << "jazab";
    else
        cout << "not jazab";
}