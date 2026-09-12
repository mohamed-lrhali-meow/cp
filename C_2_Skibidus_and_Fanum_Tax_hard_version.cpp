#include <iostream> 
#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

int bin_search(int curr, int prev, vector<int> b)
{
    int low = 0;
    int high = b.size() - 1;
    int mid ;
    int out = - 1;
    while (low <= high)
    {
        mid = (high + low) / 2;
        if (b[mid] - curr >= prev) 
        {
            high = mid - 1;
            out = mid;
        }
        else low = mid + 1; 
    }
    return out;

}

void    solve()
{
    int n, m;
    cin >> n >> m;
    vector<int> a(n);
    vector<int> b(m);
    for (int i = 0; i < n; i++) cin >> a[i];
    for (int i = 0; i < m; i++) cin >> b[i];
    sort(b.begin(), b.end());
    a[0] = min(a[0], b[0] - a[0]);
    for (int i = 1; i < n; i++)
    {
        int p1 = a[i];
        int index = bin_search(a[i], a[i - 1],b);
        int p2 = (index != - 1) ? b[index] - a[i] : INT_MAX;
        int option1 = min(p1, p2);
        int option2 = max(p1, p2);
        if (option1 >= a[i - 1]) a[i] = option1;
        else if (option2 >= a[i - 1]) a[i] = option2;
        else 
        {
            cout << "NO\n";
            return;
        }
    }
    cout << "YES\n";
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int n;
    std::cin >> n;
    for (int i = 0; i < n; i++) solve();
    return 0;
}