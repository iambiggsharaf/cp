#include <bits/stdc++.h>
using namespace std;
int main (){
    int n = 10, m = 10, cnt = 0, temp;
    vector < vector <int> > arr;
    for(int i = 0; i < n; i++){
        vector <int> row;
        for(int j = 0; j < m; j++){
            cin >> temp;
            row.push_back(temp);
        }
        arr.push_back(row);
    }
    for(int i = 0; i < n - 1; i++){
        for(int j = 0; j < m; j++){
            if(arr[i][j] == 1 and arr[i + 1][j] == 1) cnt++;
        }
    }
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m - 1; j++){
            if(arr[i][j] == 1 and arr[i][j + 1] == 1) cnt++;
        }
    }
    cout << cnt;
}
