// Ali Ghanbari
// Student Number: 4001239216

#include <iostream>
#include <fstream>
#include <cstring>
using namespace std;
char Alphabet[27] = "abcdefghijklmnopqrstuvwxyz";

void Decode(int n, char &t)
{
    for (int i = 0; i < strlen(Alphabet); i++)
        if (t == Alphabet[i])
        {
            if (i < n)
            {
                t = Alphabet[26 - (n - i)];
                break;
            }
            else
            {
                t = Alphabet[i - n];
                break;
            }
        }
}
int main()
{
    ifstream inFile("Coded_Caesar.txt");
    ofstream outFile;
    outFile.open("Decode_4001239216.txt");
    char ch;
    int n;
    cout << "<< I found out n is 4 >>" << endl
         << "enter n: ";
    cin >> n;

    while (inFile.get(ch))
    {
        if (ch >= 'a' && ch <= 'z')
        {
            Decode(n, ch);
            outFile << ch;
        }
        else
            outFile << ch;
    }
    inFile.close();
    outFile.close();
    return 0;
}
