#include <math.h>
#include <iostream>
using namespace std;

int main()
{
    int a, b, c;
    float x1, x2, delta;
    cout << "please enter three number: ";
    cin >> a >> b >> c;
    delta = b * b - 4 * a * c;
    if (delta >= 0)
    {
        x1 = (-b + sqrt(delta)) / (2 * a);
        x2 = (-b - sqrt(delta)) / (2 * a);
        cout << "x1 = " << x1 << " , x2 = " << x2;
    }
    else
        cout << "non real root";
    return 0;
}