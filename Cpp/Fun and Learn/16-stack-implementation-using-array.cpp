
#include <iostream>
#include <stdlib.h>  // for exit()

using namespace std;

#define SIZE 5

//---------------------------

class stack
{
    public:
            stack();
            int empty();
            void push_and_test(int , int&);
            void pop_and_test(int& , int&);
            void top_and_test(int& , int&);

            int sum_of_elements(int&);
            void max_min(int&, int&, int&);
            int search(int, int&);

            void display();

    private:
            int myTop;
            int items[SIZE];
};

//---------------------------

stack::stack()
{
    myTop = -1;
}

//---------------------------

int stack::empty()
{
    if(myTop == -1)
        return 1;
    else
        return 0;
}

//---------------------------

void stack::push_and_test(int x, int& overflow)
{
    if(myTop == SIZE - 1)
        overflow = 1;
    else
    {
        overflow = 0;
        items[++myTop] = x;
    }
}

//---------------------------

void stack::pop_and_test(int& x, int& underflow)
{
    if(empty())
        underflow = 1;
    else
    {
        underflow = 0;
        x = items[myTop--];
    }
}

//---------------------------

void stack::top_and_test(int& x, int& underflow)
{
    if(empty())
        underflow = 1;
    else
    {
        underflow = 0;
        x = items[myTop];
    }
}

//---------------------------

int stack::sum_of_elements(int& underflow)
{
    int s = 0;

    if(empty())
        underflow = 1;
    else
    {
        underflow = 0;
        for (int i = 0; i <= myTop ; i++)
            s += items[i];
    }

    return s;
}

//---------------------------

void stack::max_min(int& max, int& min, int& underflow)
{
    max = items[0];
    min = items[0];

    if(empty())
        underflow = 1;
    else
    {
        underflow = 0;
        for (int i = 0; i <= myTop; i++)
        {
            if(items[i] > max)
                max = items[i];
            
            if(items[i] < min);
                min = items[i];
        }
    }
}

//---------------------------

int stack::search(int x, int& underflow)
{
    if(empty())
        underflow = 1;
    else
    {
        underflow = 0;
        for(int i = 0; i <= myTop ; i++)
            if(items[i] == x)
                return i;
    }

    return -1;
}

//---------------------------

void stack::display()
{
    if(empty())
        cout << " Stack is empty" << endl;
    else
    {
        cout << endl;
        for(int i = myTop ; i >= 0; i--)
            cout << "  | " << items[i] << " |" << endl;
        cout << "  -----" << endl;
    }
}

//---------------------------

int menu();

//---------------------------

int main(){

    int x, overflow, underflow;
    int sum, max, min, index;

    stack s;

    while(1)
    {
        switch(menu())
        {
            case 1:
                s.display();
                break;

            case 2:
                cout << " Enter x to push: ";
                cin >> x;

                s.push_and_test(x, overflow);

                if(overflow)
                    cout << " Stack is full" << endl;
                else
                    cout << " Push done" << endl;
                break;

            case 3:
                s.pop_and_test(x, underflow);

                if(underflow)
                    cout << " Stack is empty" << endl;
                else
                    cout << " Popped value is: " << x << endl;
                break;

            case 4:
                s.top_and_test(x, underflow);

                if(underflow)
                    cout << " Stack is empty" << endl;
                else
                    cout << " Retrieved value is: " << x << endl;
                break;

            case 5:
                sum = s.sum_of_elements(underflow);

                if(underflow)
                    cout << " Stack is empty" << endl;
                else
                    cout << " Sum of the stack elements: " << sum << endl;
                break;

            case 6:
                s.max_min(max, min, underflow);

                if(underflow)
                    cout << " Stack is empty" << endl;
                else
                {
                    cout << " max: " << max << endl;
                    cout << " min: " << min << endl;
                }
                break;

            case 7:
                cout << " Enter x to search: ";
                cin >> x;

                index = s.search(x, underflow);

                if(underflow)
                    cout << " Stack is empty" << endl;
                else
                {
                    if(index = -1)
                        cout << " " << x << " is not in stack" << endl;
                    else
                        cout << " " << x << "found in index " << index << endl;
                }
                break;
            
            case 8:
                exit(0);  // to break while loop
                break;
        }
    }
}

//---------------------------

int menu()
{
    int s;

    cout << "__________________________" << endl;
    cout << " 1. Display stack"          << endl;
    cout << " 2. Push to stack"          << endl;
    cout << " 3. Pop from stack"         << endl;
    cout << " 4. Retrieve from stack"    << endl;
    cout << " 5. Sum of the elements"    << endl;
    cout << " 6. Max & Min of elements"  << endl;
    cout << " 7. Search stack elements"  << endl;
    cout << " 8. Exit"           << endl << endl;

    cout << " Enter your select(1-8): ";
    cin >> s;

    return s;
}

//---------------------------