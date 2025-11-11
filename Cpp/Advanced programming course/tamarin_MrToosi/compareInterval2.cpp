// A C++ program to sort vector using our own comparator
#include <bits/stdc++.h>
using namespace std;

struct area
{
    int Beginning, Finish;
};

bool compareInterval(area i1, area i2)
{
    if (i1.Finish - i1.Beginning == i2.Finish - i2.Beginning)
        return (i1.Beginning < i2.Beginning);
    else
        return (i1.Finish - i1.Beginning < i2.Finish - i2.Beginning);
}

int main()
{
    vector<area> v{{6, 8}, {1, 9}, {2, 4}, {4, 7}, {1, 2}, {9, 10}, {3, 8}};

    sort(v.begin(), v.end(), compareInterval);

    cout << "areas sorted : \n";
    for (auto x : v)
        cout << "[" << x.Beginning << ", " << x.Finish << "] ";

    return 0;
}
