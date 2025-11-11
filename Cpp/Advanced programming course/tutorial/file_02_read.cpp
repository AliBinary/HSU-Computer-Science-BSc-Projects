// در این برنامه ده عددی که در فایل بوده‌اند را خوانده و نمایش می‌دهیم
#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    int i, x;
    // خواندن اعداد از فایل
    ifstream fin("digits.txt");
    // متغیرهای ظاهری هستند x,i
    for (i = 1; i <= 10; i++)
    {
        fin >> x;
        cout << x << ",";
    }

    fin.close();
    return 0;
}