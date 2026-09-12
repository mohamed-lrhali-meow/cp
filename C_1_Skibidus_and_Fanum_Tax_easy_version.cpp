#include <iostream> 
#include <vector>
#include <algorithm>

using namespace std;

void    solve()
{
    int n, m;
    cin >> n >> m;
    vector<int> a(n);
    int b;
    for (int i = 0; i < n; i++) cin >> a[i];
    cin >> b;
    a[0] = min(a[0], b - a[0]);
    for(int i = 1 ; i < n; i++)
    {
        int p1 = a[i];
        int p2 = b - a[i];
        if (min(p1, p2) >= a[i - 1]) a[i] = min(p1, p2);
        else if (max(p1, p2) >= a[i - 1]) a[i] = max(p1, p2);
        else 
        {
            cout << "NO\n";
            return;
        }
    }
    cout << (std::is_sorted(a.begin(), a.end()) ? "YES" : "NO") << '\n';
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int n;
    std::cin >> n;
    for (int i = 0; i < n; i++) solve();
    return 0;
}