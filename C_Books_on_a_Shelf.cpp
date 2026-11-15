#include <iostream>
#include <vector> 
#include <algorithm>

#define forn(i, n) for(int i = 0; i < n; i++)
using namespace std;

void printvect(vector<int> v)
{
    for (auto x : v) cout << x << ' ';
}

void    solve()
{
    int t;
    cin >> t;
    vector<int> nums;
    vector<int> out;
    vector<int> a;
    vector<int> b;
    forn(i , t)
    {
        int x ; 
        cin >> x;
        nums.push_back(x);
    }
    sort(nums.begin(), nums.end());
    forn(i , t)
    {
        if (i == 0 || nums[i] > nums[i - 1])
            out.push_back(nums[i]);
        else
            a.push_back(nums[i]);
    }
    sort(a.begin(), a.end(), std::greater<>());
    forn(i , a.size())
    {
        if (i == 0 || a[i] < a[i - 1])
            b.push_back(a[i]);
        else
            out.push_back(a[i]);
    }
    for (auto x : b) out.push_back(x);
    cout << out.size() - (a.size() - b.size()) << endl;
    printvect(out);
    cout << endl;
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