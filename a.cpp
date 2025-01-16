#include <bits/stdc++.h>
using namespace std;
int main() {
    int ans, n, cnt = 0;
    cin >> ans >> n;
    if(n > 0){
        vector<int> arr(n);
        for(int i = 0; i < n; i++) cin >> arr[i];
        sort(arr.begin(), arr.end());
        for(int i = 0; i < n; i++){
                if(arr[i] >= ans){
                    ans = arr[i];
                    cnt = 1;
                    break;
                }
        }
        for(int i = 0; i < n; i++){
            if(arr[i] - ans >= 3){
                cnt++;
                ans = arr[i];
            }
        }
        cout << cnt;
    }
    else cout << 0;
}
