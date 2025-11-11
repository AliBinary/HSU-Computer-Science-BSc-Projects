
#include<iostream>

#include<fstream>

using namespace std;
    
int main() {
    ifstream phone_file("phone.txt");
    
    long   number;
    string name, search_name;
    
    bool found = false;
    
    cout << "Enter a name for finding its phone number: ";
    cin >> search_name;
    cout << endl;
    
    while(phone_file >> number) {
        
        phone_file >> name;
        
        if(name == search_name) {
            cout << name << " : " << number << endl;
            found = true;
            break;
        }
    }
    
    if(found == false)
        cout << search_name << " is not in this phonebook" << endl;
}