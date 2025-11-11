#include <iostream>
#include <fstream>
#include <cstring>
using namespace std;

int main()
{
    ifstream inFile("Coded_Caesar.txt");
    ofstream outFile;
    outFile.open("Decode_4001239170.txt");
    char ch;
    int n = 4;
    while (inFile.get(ch))
    {
        if (ch >= 'a' && ch <= 'z')
        {
            if ((int)ch - 97 >= n)
                ch = ((int)ch) - n;
            else
                ch = 123 - (n - (((int)ch) - 97));

            outFile << ch;
        }
        else
            outFile << ch;
    }
    inFile.close();
    outFile.close();
    return 0;
}
