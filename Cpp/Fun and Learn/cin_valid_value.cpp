#include <iostream>
using namespace std;

void cin_valid_int(int &num, string msg)
{
    bool valid = true;
    while (valid == true)
    {
        cout << msg;
        cin >> num;
        if (!cin)
        {
            cout << "\n<Enter a valid value, Try again.>\n";
            cin.clear();
            cin.ignore(100, '\n');
            continue;
        }
        else
            valid = false;
    }
}

int main()
{
    int a;
    string pm = "Hey idiot, enter a number: ";
    cin_valid_int(a, pm);
    cout << "\nAfter a few years you succeeded to enter the number "
         << a << endl;
}