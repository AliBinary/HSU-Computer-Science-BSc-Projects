#include <iostream>
using namespace std;

#define WINDOWS 1
void clrscr()
{
#ifdef WINDOWS
    system("cls");
#endif
#ifdef LINUX
    system("clear");
#endif
}

int main()
{
    cout << 123;
    cout << "yohoooooo";

    clrscr();
    cout << "oh, the screen was cleared!\n";
}