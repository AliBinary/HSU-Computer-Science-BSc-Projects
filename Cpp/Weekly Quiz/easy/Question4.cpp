#include <iostream>
using namespace std;

int main()
{
    int GPA;

    cout << "Question 4: Classification of Student based on their average.\n\n";

    cout << "Please enter your grade : ";
    cin >> GPA;

    while (GPA < 0 || GPA > 20)
    {
        cout << "\nYou have entered your grade incorrectly!" << endl
             << " please enter the grade again : ";
        cin >> GPA;
    }

    if (GPA < 10)
        cout << "\n Your score is poor!";
    else if (GPA <= 15)
        cout << "\n Your score is good!";
    else
        cout << "\n Your score is excellent!";

    return 0;
}