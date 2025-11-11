// در این برنامه بدون دانستن تعداد اعداد داخل فایل، آنها را می‌خوانیم
#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    int i, x;
    // خواندن اعداد از فایل
    ifstream fin("digits.txt");
    while (fin >> x)
    {
        cout << x << ",";
    }

    fin.close();
    return 0;
}