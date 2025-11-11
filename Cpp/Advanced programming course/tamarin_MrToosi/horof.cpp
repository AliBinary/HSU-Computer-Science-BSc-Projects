#include <iostream>
#include <time.h>
using namespace std;

int main()
{
    char horof[27] = "abcdefghijklmnopqrstuvwxyz";
    char kelid[27];
    int n;

    char temp;
    srand(time(0));
    for (int i = 0, j = 27; i < 27; i++, j--)
    {
        n = rand() % j; // n = 5, i = 0, j =27
        kelid[i] = horof[n];
        temp = horof[n];
        horof[n] = horof[j - 1];
        horof[j - 1] = temp;
    }

    for (int i = 0; i < 27; i++)
        cout << kelid[i];

    return 0;
}
