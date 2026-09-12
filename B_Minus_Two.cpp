#include <iostream> 
#include <algorithm> 
#include <vector> 

#define forn(i, n) for(int i = 0; i < n; i++)
using namespace std;

void    solve()
{
    int n{}, odd, even;
    odd = 0;
    even = 0;
    cin >> n;
    if (n == 0)
    {
        cout << "0\n";
        return;
    }
    vector<int> a(n);
    forn(i, n)
    {
        cin >> a[i];
    }
    int i = 0;
    int x;
    int c1 = 0;
    int c2 = 0;
    for(i = 0; i < n; i++)
    {
        if(a[i] % 4 == 0) c1++;
        else if (a[i] % 4 == 2) c2++;
        else odd++;
    }
    cout << max(c1, max(c2, odd)) << endl;
}
int main()
{
    int t;
    cin >> t;
    for(int i = 0; i < t; i++)
    {
        solve();
    }
    return 0;
}