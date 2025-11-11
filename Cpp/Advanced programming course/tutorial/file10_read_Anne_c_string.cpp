// در این فایل ۳۰ کلمه‌ی اول فایل کتاب آن شرلی خوانده و چاپ می‌شود
#include <iostream>
#include <fstream>
#include <cstring>
using namespace std;

int main()
{
    ifstream inFile("Anne_of_Green_Gables.txt");
    if (!inFile)
    {
        cout << "Cannot open input file";
        // به جای رترن از تابع زیر هم استفاده می‌شود. البته تفاوت مختصری با هم دارند
        exit(-1);
    }
    // فرض می‌کنیم هر کلمه حداکثر ۲۵۵ حرف دارد
    char str[256];
    int i = 0;
    while (!inFile.eof())
    {
        inFile >> str;
        cout << str << "\n";
        i++;
        if (i >= 30)
            break;
    }
    cout << "\n\n"
         << i << " words were read...";
    inFile.close();
    return 0;
}
