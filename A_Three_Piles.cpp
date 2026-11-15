#include <iostream>
#include <vector>
#include <algorithm>

using namespace std ;

void solve()
{
    vector<int> a;
    for (int i = 0; i < 3 ; i++)
    {
        int x;
        cin >> x;
        a.push_back(x);
    }
    sort(a.begin(), a.end());
    if (a[2] == a[1] + 1  && a[1] == a[0] + 1)
        cout << "YES" << endl;
    else 
        cout << "NO" << endl;
}

int main()
{
    int n ;
    cin >> n;
    for (int i = 0; i < n; i++ )
        solve();
}