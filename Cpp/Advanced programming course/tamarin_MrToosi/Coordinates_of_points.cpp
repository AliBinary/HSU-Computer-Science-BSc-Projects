#include <bits/stdc++.h>
using namespace std;

int main()
{
    int x, y;
    srand(time(0));

    for (int i = 0; i < 10; i++)
    {
        x = rand() % 101 - 50;
        y = rand() % 101 - 50;
        printf("(%3d, %3d)\n", x, y);
    }
}