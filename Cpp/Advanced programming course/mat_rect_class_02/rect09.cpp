// Mahmood Amintoosi, HSU, m.amintoosi@gmail.com
// تفاوت ارث‌بری عمومی و خصوصی
#include <iostream>
#include <string.h>
using namespace std;

#define BLACK 30
#define WHITE 97
#define RED 91
#define GREEN 92
#define YELLOW 93
#define BLUE 94


void gotoxy(int column, int row)
{
    printf("\e[%d;%df",row,column);
}

void clrscr()
{
    printf("\033[H\033[J");
}

void textcolor(int color)
{
  printf("\033[0;%d;49m", color);
}

void hidetext()
{
  printf("\033[8;39;40m");
}

class Rect
{
protected:
    int left, top, right, bottom,
        color, visible;

public:
    Rect();
    Rect(int l, int t, int r, int b,
         int c, int v);
    void draw(void);
    void show(void);
    void hide(void);
    void changeColor(int newColor);
    ~Rect();
};
//------------------ Default Constructor -------------------
Rect::Rect()
{
    left = 6;
    top = 5;
    right = 74;
    bottom = 9;
    color = WHITE;
    visible = 0;
    if (visible == 1)
        show();
}
//------------------ Constructor -------------------
Rect::Rect(int l, int t, int r, int b,
           int c, int v)
{
    left = l;
    top = t;
    right = r;
    bottom = b;
    color = c;
    visible = v;
    if (visible == 1)
        show();
}
//------------------ draw ------------------
void Rect::draw()
{
    int i, j;
    //Top line
    gotoxy(left, top);
    cout << "+";
    for (i = left + 1; i < right; i++)
        cout << "-";
    cout << "+";
    //Bottom line
    gotoxy(left, bottom);
    cout << "+";
    for (i = left + 1; i < right; i++)
        cout << "-";
    cout << "+";
    //Left line
    for (i = top + 1; i < bottom; i++)
    {
        gotoxy(left, i);
        cout << "|";
    }
    //Right line
    for (i = top + 1; i < bottom; i++)
    {
        gotoxy(right, i);
        cout << "|";
    }
}
//------------------ show ------------------
void Rect::show()
{
    textcolor(color);
    draw();
    visible = 1;
}
//------------------ hide ------------------
void Rect::hide()
{
    hidetext();
    draw();
    visible = 0;
    textcolor(WHITE);
}
//-------------- changeColor ---------------
void Rect::changeColor(int newColor)
{
    color = newColor;
    if (visible == 1)
        show();
}
//----------------- ~Rect() ---------------
Rect::~Rect()
{
    if (visible == 1)
        hide();
}

//------------ MsgBoxClass -------------
class MsgBox : public Rect
{
public:
    MsgBox(){};
    MsgBox(int l, int t, int r, int b,
           int c, int v) : Rect(l, t, r, b, c, v){};
    void show(const char *msg);
};
//----------------- show -------------------
void MsgBox::show(const char *msg)
{
    int i;
    textcolor(color);
    gotoxy((left + right) / 2 - strlen(msg) / 2, (top + bottom) / 2);
    cout << msg;
    cin.get();
    gotoxy((left + right) / 2 - strlen(msg) / 2, (top + bottom) / 2);
    for (i = 1; i <= strlen(msg); i++)
        cout << " ";
}
//------------------ main ------------------
int main()
{
    clrscr();
    Rect A(10, 1, 20, 4, RED, 1);
    MsgBox msg1(5, 10, 75, 14, GREEN, 1);
    msg1.show("Press Enter to change color of A to Yellow");
    A.changeColor(YELLOW);
    msg1.show("Press Enter to change color of Msg1's frame");
    msg1.changeColor(WHITE); // اگر ارث‌بری عمومی نباشد خطا خواهیم گرفت
	// http://www.trytoprogram.com/cplusplus-programming/access-specifiers/
    msg1.show("Press Enter to quit.");
    return 0;
}