#include <iostream>
using namespace std;

int main()
{
    int cnt_a, cnt_b, a[10], b[10], x = 0;

    for (int i = 0; i < 10; i++)
        cin >> a[i];

    for (int i = 0; i < 10; i++)
    {
        cnt_a = 0;
        for (int j = 0; j < 10; j++)
            if (a[i] == a[j])
                cnt_a++;

        if (cnt_a > 1)
        {
            b[x] = a[i];
            x++;
        }

        cnt_b = 0;
        for (int m = 0; m <= x; m++)
        {
            if (b[m] == a[i])
                cnt_b++;
        }

        if (cnt_b == 1)
            cout << a[i] << " ";
    }
}