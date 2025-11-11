#include <iostream>
using namespace std;

int main()
{

    int a, b, max;
    cout << "enter two intergers";
    cin >> a >> b;
    max = a;
    if (b > max)
        max = b;
    cout << "maximum number is :" << max << endl;
}
