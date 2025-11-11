#include <iostream>
#include <cmath>
using namespace std;

float selectUnit(string entry);

int main()
{
    float radius, surface;
    string nowUnit, newUnit;
    cout << "Question 2: Find the surface area of a sphere.\n\n";

    cout << "Please Enter the radius of a sphere with unit (Available units: Mm, Cm, Dm, Hm ,Km or m)"
         << "\n<<for example : 7 Cm>>\n";
    cin >> radius;
    cin >> nowUnit;
    while (!selectUnit(nowUnit))
    {
        cout << "\noh, this unit is unknown! please enter radius and unit again : ";
        cin >> radius;
        cin >> nowUnit;
    }

    surface = 4 * M_PI * radius * radius;

    char convert;
    cout << "\nDo you want to convert the surface unit? (y or n)\n";
    cin >> convert;
    if (convert == 'y')
    {
        cout << "\nEnter new unit:"
             << "(e.g. Mm, Cm, Dm, Hm ,Km or m)\n";
        cin >> newUnit;
        while (!selectUnit(newUnit))
        {
            cout << "\noh, this unit is unknown! please enter new unit again : ";
            cin >> newUnit;
        }
        surface = surface * selectUnit(nowUnit) / selectUnit(newUnit);
        cout << "Surface area of sphere is: " << surface << " " << newUnit;
    }
    else
        cout << "ok, Surface area of sphere is: " << surface << " " << nowUnit;
}

float selectUnit(string entry)
{
    switch (entry[0])
    {
    case 'm':
        return 1;

    case 'M':
        return 1e-3;

    case 'C':
        return 1e-2;

    case 'D':
        return 1e-1;

    case 'H':
        return 1e2;

    case 'k':
        return 1e3;
    default:
        return 0;
    }
}