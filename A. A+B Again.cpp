#include <bits/stdc++.h>
using namespace std;
int main() {
    int t, n, cnt;
    cin >> t;
    while(t--){
        cin >> n;
        cnt = 0;
        while(n){
            cnt += n % 10;
            n /= 10;
        }
        cout << cnt << "\n";
    }
}
