// AliGhanbari
// Student Number: 4001239216

#include <iostream>
#include <fstream>
#include <cstring>
using namespace std;
char horoof[37] = "abcdefghijklmnopqrstuvwxyz1234567890";
char kelid[37] = "qazwsxedcrfvtgbyhnujmikolp9512036874";
void code(char &t)
{
    for (int i = 0; i < strlen(horoof); i++)
        if (t == horoof[i])
        {
            t = kelid[i];
            break;
        }
}
int main()
{
    ifstream inFile("Anne_of_Green_Gables.txt");
    if (!inFile.is_open())
    {
        cout << "Cannot open input file";
        inFile.close();
        exit(1);
    }
    ofstream outFile;
    outFile.open("Anne_of_Green_Gables_Ramz.txt");
    if (!outFile.is_open())
    {
        cout << "Cannot open output file";
        outFile.close();
        exit(1);
    }
    char ch;
    while (inFile.get(ch))
    {
        ch = tolower(ch);
        code(ch);
        cout << ch;
        outFile << ch;
    }
    outFile << endl
            << 4001239216;
    inFile.close();
    outFile.close();
    return 0;
}
