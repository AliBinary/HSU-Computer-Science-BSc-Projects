// Mahmood Amintoosi, HSU, m.amintoosi@gmail.com
// Destructor
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
private:
    int left, top, right, bottom,
        color, visible;

public:
    Rect(int l, int t, int r, int b,
         int c, int v);
    void draw(void);
    void show(void);
    void hide(void);
    void changeColor(int newColor);
    ~Rect();
};

void msgBox(int l, int t, int r, int b,
            int c, const char *msg);
//------------------ Constructor -------------------
// void is dropped
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

//----------------- msgBox -----------------
void msgBox(int l, int t, int r, int b,
            int c, const char *msg)
{
    Rect box(l, t, r, b, c, 1);
    int i;
    // box.set(l, t, r, b, c, 1);
    gotoxy((l + r) / 2 - strlen(msg) / 2, (t + b) / 2);
    cout << msg;
    cin.get();
    gotoxy((l + r) / 2 - strlen(msg) / 2, (t + b) / 2);
    for (i = 1; i <= strlen(msg); i++)
        cout << " ";
}
//------------------ main ------------------
int main()
{
    clrscr();
    Rect A(10, 1, 20, 4, RED, 1);
        // B(30, 3, 60, 7, BLUE, 0);
    msgBox(5, 10, 75, 14, GREEN, "Press Enter to change color of A to Yellow");
    A.changeColor(YELLOW);
    {
        Rect B(30, 3, 60, 7, BLUE, 0);
        msgBox(5, 10, 75, 14, GREEN, "Press Enter to show B");
        B.show();
        msgBox(5, 10, 75, 14, GREEN, "Press Enter to automatically hide B");
    }
    msgBox(5, 10, 75, 14, GREEN, "Press Enter to quit. A would be hidden.");
    return 0;
    // بعد از اتمام برنامه، خط فرمان دیده نمی‌شود!
    // ملاحظه شود hide تابع
}