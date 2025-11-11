#include <iostream>
#include <fstream>
using namespace std;
// این برنامه تصویر پرچم ایران را تولید می‌کند.
// تصویر خروجی را با برنامه  زیر باز کنید:
// IrfanView
int main()
{
    int i, j, h = 150, w = 200;
    ofstream fout;
    fout.open("parcham.ppm");
    fout << "P3" << endl;
    fout << w << " " << h << endl;
    fout << "255" << endl;

    for (i = 0; i < 50; i++)
    {
        for (j = 0; j < 200; j++)
            fout << "0 255 0 ";
        fout << endl;
    }

    for (i = 0; i < 50; i++)
    {
        for (j = 0; j < 200; j++)
            fout << "255 255 255 ";
        fout << endl;
    }

    for (i = 0; i < 50; i++)
    {
        for (j = 0; j < 200; j++)
            fout << "255 0 0 ";
        fout << endl;
    }

    fout.close();
    return 0;
}
