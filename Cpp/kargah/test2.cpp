#include <iostream>
using namespace std;

int main()
{
    float r, s, p;
    cin >> r;
    const float PI = 3.145292;
    p = r * 2 * PI;
    s = (r * r) * PI;
    cout << p << endl
         << s;
}