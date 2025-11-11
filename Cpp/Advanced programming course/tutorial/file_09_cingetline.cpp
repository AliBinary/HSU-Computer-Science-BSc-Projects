// این برنامه ربط مستقیم به خواندن از فایل ندارد. تفاوت دو نوع خواندن رشته ها
#include <iostream>
using namespace std;

int main()
{
    char str[256];
    cin >> str; // hello world - > hello
    // cin.getline(str,255); // hello world - > hello world
    cout << str;
    return 0;
}
