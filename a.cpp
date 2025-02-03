#include <bits/stdc++.h>
using namespace std;

bool comparison (pair <int, int> a, pair <int, int> b) {

         return (a.second == b.second) ? a.first < b.first : a.second > b.second;

}
int main(){
    long long int n, a, b ;
    cin >> n;
    vector<pair<int, int>> arr;
    for(int i = 0; i < n; i++){
        cin >> a >> b;
        arr.push_back({a, b});
    }
    sort(arr.begin(), arr.end(), comparison);
    for(int i = 0; i < n; i++){
        cout << arr[i].first << " " << arr[i].second<< "\n";
    }

}
