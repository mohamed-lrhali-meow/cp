#include <iostream>
#include <vector> 
#include <algorithm>

#define forn(i, n) for(int i = 0; i < n; i++)
using namespace std;


void    solve()
{
    int n, m;
    cin >> n >> m;

    vector<int> a(n);
    vector<int> b(m);

    for (int i = n - 1; i >= 0; i--) {
        cin >> a[i];
    }

    for (int i = m - 1; i >= 0; i--) {
        cin >> b[i];
    }
    int sa = a[0];
    int sb = b[0];
    for (int i = 1; i < n; i++)
    {
        sa += a[i]- a[i - 1] + 1;
    }
    for (int i = 1; i < m; i ++)
    { 
        sb += b[i] - b[i - 1]  + 1;
    }
    cout <<( (sa >= sb) ? '1' : '2' )<< endl; 
    
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