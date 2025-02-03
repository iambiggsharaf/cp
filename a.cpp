#include <bits/stdc++.h>
using namespace std;
bool comparison (pair <string, double> a, pair <string, double> b) {
         return a.second > b.second;
}
int main(){
    double n, x, y, z;
    string a, b;
    cin >> n;
    vector <pair<string,double>>arr;
    for(int i = 0; i < n; i++){
        cin >> a >> b >> x >> y >> z;
        a += " "+b;
        x = (x+y+z)/3;
        arr.push_back({a, x});
    }
    sort(arr.begin(), arr.end(), comparison);
    for(auto i:arr) cout << i.first << "\n";
}
