// در این فایل ۳۰۰ حرف اول فایل کتاب آن شرلی خوانده و چاپ می‌شود
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
        return -1;
    }
    // فرض می‌کنیم هر خط حداکثر ۲۵۵ حرف دارد
    char ch;
    int i = 0;
    while (!inFile.eof())
    {   
        // تفاوت دو دستور زیر را بررسی فرمایید.
        // inFile >>ch; 
        inFile.get(ch);
        cout << ch;
        i++;
        if (i >= 300)
            break;
    }
    cout << "\n\n"
         << i << " characters were read...";
    inFile.close();
    return 0;
}
