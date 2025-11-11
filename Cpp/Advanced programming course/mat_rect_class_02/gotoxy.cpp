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

//------------------ main ------------------
int main()
{
  clrscr();
  for(int i=1; i<= 5; i++)
  {
      gotoxy(i,i);
      cout << "*";
  }
  cout << endl;
  return 0;
}