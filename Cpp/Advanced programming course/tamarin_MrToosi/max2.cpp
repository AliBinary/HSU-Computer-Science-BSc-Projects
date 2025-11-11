#include <iostream>
using namespace std;

int main()
{
    int max1, max2, a[10];
    for (int i = 0; i < 10; i++)
        cin >> a[i];

    max1 = a[0];
    max2 = NULL;
    for (int i = 0; i < 10; i++)
        if (a[i] > max1)
            max1 = a[i];

    for (int i = 0; i < 10; i++)
        if (a[i] != max1 && a[i] > max2)
            max2 = a[i];

    cout << max2;
}