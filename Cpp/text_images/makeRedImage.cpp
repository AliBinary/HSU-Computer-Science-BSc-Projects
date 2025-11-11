#include <iostream>
#include <fstream>
using namespace std;
// برنامه تولید یک مستطیل قرمز
int main()
{
    const int N = 360;
    float q[N]={0}, x;
    int i,j;
    ofstream fout;
    fout.open("ghermez.ppm");
    fout << "P3" << endl;
    fout << "200 100" << endl;
    fout << "255" << endl;
    for (i = 0; i < 100; i++)
    {
        for(j=0;j<200;j++)
            fout << "255 0 0 ";
        fout << endl;    
    }
    fout.close();    
    return 0;
}
