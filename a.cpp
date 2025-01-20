#include <bits/stdc++.h>
using namespace std;
int main() {
    long long n, q, l, r, cnt = 0, num;
    cin >> n >> q;
    vector<long long> arr;
    arr.push_back(cnt);
    while(n--){
        cin >> num;
        cnt += num;
        arr.push_back(cnt);
    }
    //for(auto i: arr) cout << i << " ";
    cout << endl;
    while(q--){
        cin >> l >> r;
        cout << arr[r] - arr[l - 1] << endl;
    }

}
