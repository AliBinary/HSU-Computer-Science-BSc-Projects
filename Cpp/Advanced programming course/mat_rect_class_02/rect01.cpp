// Mahmood Amintoosi, HSU, m.amintoosi@gmail.com
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
public:
  int left, top, right, bottom,
      color, visible;
};

void set(Rect &R, int l, int t, int r, int b,
         int c, int v);
void draw(Rect R);
void show(Rect &R);
void hide(Rect &R);
void changeColor(Rect &R, int newColor);
void msgBox(int l, int t, int r, int b,
            int c, const char *msg);
//------------------ set -------------------
void set(Rect &R, int l, int t, int r, int b,
         int c, int v)
{
  R.left = l;
  R.top = t;
  R.right = r;
  R.bottom = b;
  R.color = c;
  R.visible = v;
  if (R.visible == 1)
    show(R);
  else
    hide(R);
}
//------------------ draw ------------------
void draw(Rect R)
{
  int i, j;
  //Top line
  gotoxy(R.left, R.top);
  cout << "+";
  for (i = R.left + 1; i < R.right; i++)
    cout << "-";
  cout << "+";
  //Bottom line
  gotoxy(R.left, R.bottom);
  cout << "+";
  for (i = R.left + 1; i < R.right; i++)
    cout << "-";
  cout << "+";
  //Left line
  for (i = R.top + 1; i < R.bottom; i++)
  {
    gotoxy(R.left, i);
    cout << "|";
  }
  //Right line
  for (i = R.top + 1; i < R.bottom; i++)
  {
    gotoxy(R.right, i);
    cout << "|";
  }
}
//------------------ show ------------------
void show(Rect &R)
{
  textcolor(R.color);
  draw(R);
  R.visible = 1;
}
//------------------ hide ------------------
void hide(Rect &R)
{
  hidetext();
  draw(R);
  R.visible = 0;
  textcolor(WHITE);
}
//-------------- changeColor ---------------
void changeColor(Rect &R, int newColor)
{
  R.color = newColor;
  if (R.visible == 1)
    show(R);
}
//----------------- msgBox -----------------
void msgBox(int l, int t, int r, int b,
            int c, const char *msg)
{
  Rect box;
  int i;
  set(box, l, t, r, b, c, 1);
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
  Rect A, B;
  clrscr();
  set(A, 10, 2, 20, 5, RED, 1);
  set(B, 30, 3, 60, 7, BLUE, 0);
  msgBox(5, 10, 75, 14, GREEN, "Press Enter to change color of A to Yellow");
  changeColor(A, YELLOW);
  msgBox(5, 10, 75, 14, GREEN, "Press Enter to show B");
  show(B);
  msgBox(5, 10, 75, 14, GREEN, "Press Enter to hide A");
  hide(A);
  msgBox(5, 10, 75, 14, GREEN, "Press Enter to quit.");
  return 0;
}