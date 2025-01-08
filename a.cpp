#include <bits/stdc++.h>
using namespace std;
int main (){
    int n;
    cin >>n;
    vector < vector <int> > arr;

    for(int i = 0 ; i < n; i++){
        vector <int> row;
        for(int j = 0; j < n; j++){
            if(i == j or i + j == n - 1) row.push_back(1);
            else row.push_back(0);
        }
        arr.push_back(row);
    }

    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            cout << arr[i][j];
        }
        cout << endl;
    }

    return 0;
}
