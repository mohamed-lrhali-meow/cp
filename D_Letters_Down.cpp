#include <iostream>
#include <vector> 
#include <algorithm>

#define forn(i, n) for(int i = 0; i < n; i++)
using namespace std;

void match(string &s, char c, int x)
{
    forn(i , s.size())
    {
        if (s[i] == c)
            s[i] -= x;
    }
}

void    solve()
{
    int n;
    cin >> n;
    string s;
    vector<bool> need(26);
    cin >> s;
    forn(i, n / 2)
    {
        char u = min(s[i], s[n - 1 - i]);
        char z = max(s[i], s[n - 1 - i]);
        for (char c = u ; c < z ; c++)
        {
            need[c - 'a'] = true;
        }
    }
    cout << count(need.begin(), need.end(), true) << endl;
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