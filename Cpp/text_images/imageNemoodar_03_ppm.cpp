#include <iostream>
#include <fstream>
#include <algorithm>
#include <ctime>
#include <cmath>
using namespace std;

const int N = 150;

void nemoodar(int a[][N], char picFileName[] = "Aks.pgm", 
    int n = N, int nc=N)
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

    imOut << "P3\n";
    imOut << width << " " << height << endl;
    imOut << nc << endl;
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
            imOut << a[i][j] << ' '<< 0 << ' '<< 0 << ' ';
        imOut << "\n";
    }
    imOut.close();
}

int main()
{
    int q[N][N] = {0};
    int i, j;
    ofstream fout;
    char picFileName[] = "nemoodar03.ppm";
    int k =0;
    for (i = 0; i < N; i++)
        for (j = 0; j < N; j++)
            q[i][j] = j;
            // q[i][j] = sqrt(i*i+j*j);//i;
            // q[i][j] = rand()%N;//i;
            // if(sqrt(i*i+j*j)<N) q[i][j] = N;//i;
            // q[i][j] = k++;

    nemoodar(q, picFileName, N);//,N*N);
    return 0;
}
