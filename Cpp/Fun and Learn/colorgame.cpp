#include <iostream>
#include <windows.h>
using namespace std;

int main()
{
    Sleep(500);

    string str;
    char num = 49;
    while (true)
    {
        system("cls");
        for (int i = 0; i < 100; i++)
        {
            cout << "this is color " << num << '\n';
        }

        str = "color ";
        str += num++;
        const char *ch = str.c_str();
        system(ch);

        Sleep(1000);

        if (num > 57 && num < 65)
            num = 65;
        else if (num > 70)
            num = 49;
    }

    return 0;
}