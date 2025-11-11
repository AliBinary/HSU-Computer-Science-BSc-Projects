#include <iostream>
#include <fstream>
#include <algorithm>
#include <ctime>
using namespace std;

const int N = 300;

void nemoodar(int a[][N], char picFileName[], int n)
{
    int width, height, i, j;
    ofstream imOut(picFileName);

    if (!imOut.is_open())
    {
        cout << "Could not open file: " << picFileName;
        return;
    }
    width = n;
    height = n;

    imOut << "P1\n";
    imOut << width << " " << height << endl;

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
            imOut << a[i][j] << ' ';
        imOut << endl;
    }
    imOut.close();
}

int main()
{
    int q[N][N] = {0};
    int i;
    ofstream fout;
    char picFileName[] = "nemoodar01.pbm";

    for (i = 0; i < N; i++)
        q[i][i] = 1;
    nemoodar(q, picFileName, N);
    return 0;
}
