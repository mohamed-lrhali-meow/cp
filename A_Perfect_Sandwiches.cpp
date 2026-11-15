#include <iostream> 




void solve()
{
    int a , b;
    std::cin >> a >> b;
    int c = 0;
    if (a <= b)
        std::cout << -1 << std::endl;
    else
        std::cout << std::min(b, a - b) << std::endl;
}



int main()
{
    int t;
    std::cin >> t; 
    for (int i = 0 ; i < t; i++)
    {
        solve();
    }
}