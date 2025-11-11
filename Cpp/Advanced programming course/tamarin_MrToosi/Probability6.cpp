#include <iostream>
#include <iomanip>
#include <ctime>
using namespace std;

int main()
{
    int num, sum = 0;

    srand(time(0));
    for (int i = 0; i < 3000; i++)
    {
        num = rand() % 6 + 1;
        if (num == 6)
            sum++;
    }

    float answer;
    answer = sum / 3000.0;

    cout << fixed << setprecision(2);
    cout << answer;
}