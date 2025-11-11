#include <iostream>
using namespace std;

bool prime(int);

int main()
{
    int X, num, max = 0;
    cin >> X;
    const int x = X;
    int nums[x];

    for (int i = 0; i < x; i++)
    {
        cin >> nums[i];
    }

    for (int i = 0; i < x; i++)
    {
        int cnt = 0;
        for (int j = 1; j < nums[i]; j++)
        {
            if (nums[i] % j == 0)
            {
                if (prime(j))
                    cnt++;
            }
        }
        if (cnt > max)
        {
            num = nums[i];
            max = cnt;
        }
    }
    cout << num << " " << max;
}

bool prime(int num)
{
    bool flag = true;
    for (int i = 2; i < num; i++)
    {
        if (num % i == 0)
        {
            flag = false;
            break;
        }
    }

    return flag;
}