// در این برنامه بدون دانستن تعداد اعداد داخل فایل، آنها را می‌خوانیم
#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    int i, x;
    // خواندن اعداد از فایل
    ifstream fin("digits.txt");
    // قبل از کار کردن با فایل چک می‌کنیم که فایل به درستی باز شده باشد
    // همین کار باید برای همه فایلهایی که باز می‌کنیم انجام شود،
    // چه برای خواندن، چه برای نوشتن
    // برای امتحان نام فایل را عوض کنید
    if (!fin)
    {
        cout << "Error: cannot open input file" << endl;
        return -1;
    }

    // خواندن تا زمانی که به انتهای فایل نرسیده‌ایم
    while (!fin.eof())
    {
        fin >> x;
        cout << x << ",";
    }

    fin.close();
    return 0;
}