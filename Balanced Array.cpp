#include <bits/stdc++.h>
using namespace std;
int main() {
    long long int t, n, cnt = 0;
    cin >> t;
    while(t--){
        cnt = 0;
        cin >> n;
        if((n / 2) % 2 != 0) cout << "NO\n";
        else{
            cout << "YES\n";
            for(int i = 1; i <= (n / 2); i++){
                cout << i * 2 << " ";
                cnt += i * 2;
            }
            for(int i = 1; i < (n / 2); i++){
                cout << i * 2 - 1 << " ";
                cnt -= i * 2 - 1;
            }
            cout << cnt << "\n";
        }
    }
}
