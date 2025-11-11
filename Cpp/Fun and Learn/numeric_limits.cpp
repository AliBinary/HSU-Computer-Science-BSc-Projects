#include <iostream>
#include <limits>
using namespace std;

int main()
{
    cout << "max value for short int :" << numeric_limits<short int>::max() << endl;
    cout << "max value for int :" << numeric_limits<int>::max() << endl;
    cout << "max value for long int :" << numeric_limits<long int>::max() << endl;
    cout << "max value for long long int :" << numeric_limits<long long int>::max() << endl;
}