#include <bits\stdc++.h>
#include <windows.h>
using namespace std;

const int N = 30;

int units[N], x;
float grades[N];
string msg;

void cin_valid_int(int &num, string msg)
{
    bool valid = true;
    while (valid == true)
    {
        cout << msg;
        cin >> num;
        if (!cin)
        {
            cout << "\n<Enter a valid value, Try again.>";
            cin.clear();
            cin.ignore(100, '\n');
            continue;
        }
        else
            valid = false;
    }
}
void cin_valid_float(float &num, string msg)
{
    bool valid = true;
    while (valid == true)
    {
        cout << msg;
        cin >> num;
        if (!cin)
        {
            cout << "\n<Enter a valid value, Try again.>";
            cin.clear();
            cin.ignore(100, '\n');
            continue;
        }
        else
            valid = false;
    }
}

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

void get(int i)
{
    clrscr();
    string cnt;
    if (i == x - 1)
    {
        cnt = "last";
    }
    else
    {
        switch (i)
        {
        case 0:
            cnt = "1st";
            break;

        case 1:
            cnt = "2nd";
            break;

        case 2:
            cnt = "3rd";
            break;

        default:
            cnt = to_string(i + 1) + "th";
            break;
        }
    }

    msg = "\nEnter the grade of the " + cnt + " lesson: ";
    cin_valid_float(grades[i], msg);

    msg = "\nEnter The number of units of this lesson: ";
    cin_valid_int(units[i], msg);
}

void GPA(int x)
{
    float sum = 0, sum_units = 0, ans;
    for (int i = 0; i <= x; i++)
    {
        sum += grades[i] * units[i];
        sum_units += units[i];
    }
    ans = sum / sum_units;
    cout << ans;
}

int main()
{
    clrscr();
    cout << "Hello, welcome to the GPA calculation program.\n";
    msg = "\n How many lessons do you want to enter? ";
    cin_valid_int(x, msg);

    for (int i = 0; i < x - 1; i++)
    {
        get(i);
        clrscr();
        cout << "\n###  So far the GPA is equal to: ";
        GPA(i);
        Sleep(700);
        clrscr();
        cout << "\n##  #So far the GPA is equal to: ";
        GPA(i);
        Sleep(700);
        clrscr();
        cout << "\n#  ##So far the GPA is equal to: ";
        GPA(i);
        Sleep(700);
        clrscr();
        cout << "\n  ###So far the GPA is equal to: ";
        GPA(i);
        Sleep(700);
    }
    get(x - 1);
    clrscr();
    cout << "\n\t--> Your final GPA is equal to: ";
    GPA(x - 1);
    cout << "\n\nI hope you enjoyed this program and it was useful for you <<3";
}