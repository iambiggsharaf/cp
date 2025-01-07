#include <bits/stdc++.h>
using namespace std;
int main() {
    int n, x;
    cin >> n;
    vector<vector<int>> a;
    for(int i = 0; i < n; i++){
        vector<int> row;
        for(int j = 0; j < n; j++){
            if(j >= n / 2) row.push_back(1);
            else row.push_back(0);
        }
        a.push_back(row);
    }
    for(auto i: a){
        for(auto j: i){
            cout << j;
        }
        cout << "\n";
    }
 }
