#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    string entry;
    cin >> entry;
    // Create and open a text file
    ofstream MyFile("love.txt");
    // Write to the file
    MyFile << entry;
    // Close the file
    MyFile.close();
}