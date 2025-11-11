#include <iostream>
using namespace std;

int oneDigit(int num)
{
    return (num >= 0 && num < 10);
}

bool isPalUtil(int num, int *dupNum)
{
    if (oneDigit(num))
        return (num == (*dupNum) % 10);
    if (!isPalUtil(num / 10, dupNum))
        return false;
    *dupNum /= 10;
    return (num % 10 == (*dupNum) % 10);
}
int isPal(int num)
{
    if (num < 0)
        num = -num;
    int *dupNum = new int(num);
    return isPalUtil(num, dupNum);
}
int main()
{
    int n;
    cout << "enter n :";
    cin >> n;
    isPal(n) ? cout << "The number is a palindrome." : cout << "The number is not a palindrome.";
    return 0;
}
