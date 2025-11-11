#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    ifstream iFile("input.txt");

    while (true)
    {
        int x;
        iFile >> x;
        if (iFile.eof())
            break;
        cerr << x << endl;
    }

    return 0;
}