// در این فایل ۳۰ خط اول فایل کتاب آن شرلی خوانده و چاپ می‌شود
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
    char str[256];
    int i = 0;
    while (!inFile.eof())
    {   
        // inFile >> str; این دستور را حذف می‌کنیم
        inFile.getline(str, 255);
        cout << str << "\n";
        i++;
        if (i >= 30)
            break;
    }
    cout << "\n\n"
         << i << " lines were read...";
    inFile.close();
    return 0;
}
