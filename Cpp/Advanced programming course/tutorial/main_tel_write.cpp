
#include<iostream>

#include<fstream>

using namespace std;
    
int main() {
    
    ofstream phone_file("phone.txt");
    
    long   number;
    string name;
    
    cout << "Enter a number for each name (0 for quit)" << endl;
    
    for( ; ; ) {
        
        cout << "Number: ";
        cin  >> number;
        
        if(number == 0)
            break;
        
        phone_file << number << ' ';
        
        cout << "Name: ";
        cin  >> name;
        
        phone_file << name << ' ';
        
        cout << endl;
    }
}