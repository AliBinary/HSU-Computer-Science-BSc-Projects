// Mahmood Amintoosi, HSU, m.amintoosi@gmail.com
// Inheritance ارث‌بری
// در این برنامه کلاس پیام از کلاس مستطیل مشتق می‌شود
// کلاس جدید فقط سازنده‌ی پیش‌فرض را دارد.
#include <iostream>
#include <string.h>
using namespace std;


class Rect
{
public:
    Rect();
};
//------------------ Default Constructor -------------------
Rect::Rect()
{
    cout << "Constructor of Rect\n";
}
//------------ MsgBoxClass -------------
class MsgBox : Rect
{
public:
    MsgBox(){cout << "Constructor of MsgBox\n"; };
};
//------------------ main ------------------
int main()
{
    MsgBox msg1;
    return 0;
}
