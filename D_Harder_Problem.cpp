#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int t;
    cin >> t;
    
    while (t--) {
        int n;
        cin >> n;
        
        vector<int> a(n);
        for (int i = 0; i < n; i++) cin >> a[i];
        
        set<int> a_set(a.begin(), a.end());
        set<int> seen;
        
        vector<int> fillers;
        for (int v = 1; v <= n; v++) {
            if (a_set.find(v) == a_set.end()) {
                fillers.push_back(v);
            }
        }
        
        int filler_idx = 0;
        vector<int> b;
        
        for (int i = 0; i < n; i++) {
            if (seen.find(a[i]) == seen.end()) {
                b.push_back(a[i]);
                seen.insert(a[i]);
            } else {
                b.push_back(fillers[filler_idx]);
                filler_idx++;
            }
        }
        
        for (int i = 0; i < n; i++) {
            cout << b[i];
            if (i < n-1) cout << " ";
        }
        cout << "\n";
    }
    
    return 0;
}