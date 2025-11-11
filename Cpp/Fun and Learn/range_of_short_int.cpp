#include <iostream>
#include <typeinfo>
using namespace std;

int get_target(short int n, int max, int step)
{
    do
    {
        cout << n << endl;
        max += step;
        n = max;
    } while (n == max);

    if (step == 1)
        return (max - 1);
    else
    {
        max -= step;
        n = max;
        step /= 10;
        return get_target(n, max, step);
    }
}

int main()
{
    short int n = 0;
    int max = 0;
    int step = 10e5;
    max = get_target(n, max, step);

    string data_type = typeid(n).name();
    if (data_type == "s")
        data_type = "short int";
    if (data_type == "i")
        data_type = "int";
    if (data_type == "c")
        data_type = "char";

    cout << "\nthe variable type was: " << data_type;
    cout << "\nthe maximum possible value was: " << max;
    cout << "\nSo, the minimum possible value is: " << -(max + 1) << "\n\n";

    return 0;
}