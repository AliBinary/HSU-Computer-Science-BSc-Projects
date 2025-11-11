// M.Amintoosi
 
#include <iostream>
using namespace std;

#define TOOL 5
 
void gotoxy(int column, int row)
{
    printf("\e[%d;%df",row,column);
}

void clrscr()
{
    printf("\033[H\033[J");
}
 
 
int main()
{
	clrscr();
	int i, j;
	// خط افقی بالا
	for (i = 1; i <= TOOL; i++)
	{
		gotoxy(i,1);
		cout << "*";	
	}

	// قطر فرعی
	for (i = 1; i <= TOOL; i++)
	{
		gotoxy(i,TOOL-i+1);
		cout << "*";	
	}

	// خط افقی پایین	
	for (i = TOOL; i >= 1; i--)
	{
		gotoxy(i,TOOL);
		cout << "*";	
	}

	return 0;
}