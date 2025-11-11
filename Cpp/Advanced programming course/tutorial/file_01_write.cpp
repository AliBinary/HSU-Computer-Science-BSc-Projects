// در این برنامه مربع تعدادی عدد را در صفحه نمایش چاپ می‌کنیم، سپس
// به صورت مشابه آنها را در فایل می‌نویسیم
#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    // چاپ مربع اعداد از ۱ تا ۱۰
    int i;
    for (i = 1; i <= 10; i++)
        cout << i*i << " ";

    // نوشتن مربع اعداد از ۱ تا ۱۰ در فایل
    ofstream fout("digits.txt");
    for (i = 1; i <= 10; i++)
        fout << i*i << " ";
        
    fout.close();
    return 0;
}