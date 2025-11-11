#include <iostream>
using namespace std;

int main()
{
    int rep, num, max = 0, a[10];

    for (int i = 0; i < 10; i++)
        cin >> a[i];

    for (int i = 0; i < 10; i++)
    {
        rep = 0;
        for (int j = 0; j < 10; j++)
            if (a[i] == a[j])
                rep++;
        if (rep > max)
        {
            max = rep;
            num = a[i];
        }
    }
    cout << num;
}