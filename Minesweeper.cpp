#include <bits/stdc++.h>
using namespace std;
int main (){
    int n = 12, m = 12, temp;
    vector<vector<int>> arr(n, vector<int>(m, 0));
    vector<vector<int>> arr1(n, vector<int>(m, 0));
    for(int i = 1; i < n - 1; i++){
        for(int j = 1; j < m - 1; j++){
            cin >> temp;
            arr[i][j] = temp;
        }
    }

    for(int i = 1; i < n - 1; i++){
        for(int j = 1; j < m - 1; j++){
            if(arr[i][j] == 0)
            arr1[i][j] = bool(arr[i - 1][j]) + bool(arr[i + 1][j]) +
             bool(arr[i][j - 1]) + bool(arr[i][j + 1]) +
             bool(arr[i + 1][j + 1]) + bool(arr[i - 1][j - 1]) +
             bool(arr[i + 1][j - 1]) + bool(arr[i - 1][j + 1]);
        }
    }

    for(int i = 1; i < n - 1; i++){
        for(int j = 1; j < m - 1; j++){
            if(arr1[i][j] == 0) cout << arr[i][j] << " ";
            else cout << arr1[i][j] << " ";
        }
        cout << endl;
    }
}
