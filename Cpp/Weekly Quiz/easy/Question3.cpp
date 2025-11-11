#include <iostream>
using namespace std;

int main()
{
    float Celsius, Kelvin, Fahrenheit;
    cout << "Question 3: Temperature conversion from Celsius to Fahrenheit and Kelvin.\n\n";

    cout << "Enter the Temperature in Celsius: ";
    cin >> Celsius;

    Kelvin = Celsius + 273.15;
    Fahrenheit = 1.8 * Celsius + 32;

    cout << "\n Equivalent Temperature in Fahrenheit : " << Fahrenheit << endl;
    cout << " Equivalent Temperature in Kelvin : " << Kelvin << endl;

    return 0;
}