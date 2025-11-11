#include <stdio.h>
using namespace std;

int main()
{
    for (int i = 0, j = 27; i <= 27, j >= 0; i++, j--)
        printf("i = %-2d and j = %2d\n", i, j);

    return 0;
}