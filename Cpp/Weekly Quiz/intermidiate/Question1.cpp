#include <iostream>
using namespace std;

void string_frequency(string str)
{
    int j, J, i = 0, alphabet[26] = {0}, Alphabet[26] = {0};
    while (str[i] != '\0')
    {
        if (str[i] >= 'a' && str[i] <= 'z')
        {
            j = str[i] - 'a';
            ++alphabet[j];
        }
        else if (str[i] >= 'A' && str[i] <= 'Z')
        {
            J = str[i] - 'A';
            ++Alphabet[J];
        }
        ++i;
    }
    cout << "\nFrequency of all alphabets in the string is:" << endl;
    for (i = 0; i < 26; i++)
        printf("%c : %-2d ,  %c : %-2d\n", char(i + 'a'), alphabet[i], char(i + 'A'), Alphabet[i]);
}

int main()
{
    string str;
    cout << "Please Enter a string : ";
    cin >> str;
    string_frequency(str);

    return 0;
}