#include <bits/stdc++.h>
using namespace std;
int main() {
    int n;
    cin >> n;
    vector<vector<int>> a;
    for(int i = 0; i < n; i++){
        vector<int> row;
        for(int j = 0; j < n; j++){
            if(i == 0 or
               j == n - 1 or
               j == 0 or
               i == n - 1) row.push_back(1);
            else row.push_back(0);
        }
        a.push_back(row);
    }
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            cout << a[i][j];
        }
        cout << endl;
    }
}

