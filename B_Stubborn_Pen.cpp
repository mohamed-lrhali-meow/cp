#include <iostream>
#include <vector> 
#include <algorithm>

#define forn(i, n) for(int i = 0; i < n; i++)
using namespace std;


void    solve()
{
    int n;
    cin >> n;
    string s;
    cin >> s;
    int c = 0;
    if (s[0] == 'B')
        c++;
    forn(i, n - 1)
    {
        if (s[i] == s[i + 1])
            c++;
    }
    cout << c << endl;
}

int main()
{
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int t;
    cin >> t;
    forn(i, t)
    {
        solve();
    }
}