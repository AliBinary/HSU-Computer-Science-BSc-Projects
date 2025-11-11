// در این برنامه بدون دانستن تعداد اعداد داخل فایل، آنها را می‌خوانیم
#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    int i, x;
    // خواندن اعداد از فایل
    ifstream fin("digits.txt");
    // خواندن تا زمانی که به انتهای فایل نرسیده‌ایم
    while (!fin.eof())
    {
        fin >> x;
        cout << x << ",";
    }

    fin.close();
    return 0;
}