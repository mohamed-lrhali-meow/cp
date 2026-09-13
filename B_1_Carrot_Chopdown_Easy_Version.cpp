#include <iostream> 
#include <algorithm> 
#include <vector> 

#define forn(i, n) for(int i = 0; i < n; i++)
using namespace std;

void    solve()
{
    int n, m;
    cin >> n >> m;
    vector<int> a(n);
    forn(i, n)
    {
        cin >> a[i];
    }
    int c = 0;
    int maxx = 0;
    for(int i = 1; i <= m; i++)
    {
        c = 0;
        forn(j, n)
        {
            if (a[j] == 2 * i)c++;
            if (a[j] >= i)c++;
        }
        maxx = max(maxx, c);
    }
    cout << maxx << endl;

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