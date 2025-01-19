#include <bits/stdc++.h>
using namespace std;
int main() {
    long long int n, cur, a, b, mod = 1791791791, maxx = -1, index = 0, index2 = 0;
    cin >> n >> cur >> a >> b;
    vector<int> arr;
    for(int i = 0; i < n; i++){
        cur = (cur * a + b) % mod;
        arr.push_back(cur);
        if(cur > maxx){
            maxx = cur;
            index = i + 1;
        }
    }
    maxx = -1;
    for(int i = 0; i < n; i++){
        if(arr[i] > maxx and i != index - 1){
            maxx = arr[i];
            index2 = i + 1;
        }
    }
    cout << index << " " << index2;
}
