#include <bits/stdc++.h>
using namespace std;
bool comparison (pair <string, int> a, pair <string, int> b) {
         return a.second < b.second;
}
int main(){
    long long int n, a, b ;
    cin >> n;
    vector<pair<string, int>> arr;
    for(int i = 0; i < n; i++){
        cin >> a >> b;
        string ans = to_string(a) + " " + to_string(b);
        double c = sqrt(pow(a, 2)+pow(b,2));
        arr.push_back({ans,c});
    }
    sort(arr.begin(), arr.end(), comparison);
    for(int i = 0; i < n; i++){
       cout << arr[i].first << "\n";
//            cout << arr[i] << " " ;
    }
}
