#include <iostream>
#include <stack>

using namespace std;

int main()
{
    stack<int> ali;
    ali.push(1);
    ali.push(2);
    ali.push(5);
    ali.push(69);

    cout << endl
         << "size of stack is : " << ali.size() << '\n';

    while (!ali.empty())
    {
        cout << ali.top() << " ";
        ali.pop();
    }

    cout << endl
         << "size of stack is : " << ali.size();
}