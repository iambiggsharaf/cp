#include <bits/stdc++.h>
using namespace std;
int main (){
    int n = 8, temp, x, y;
    //cin >>n;
    vector < vector <int> > arr;
    for(int i = 0 ; i < n; i++){
        vector <int> row;
        for(int j = 0; j < n; j++){
            cin >> temp;
            row.push_back(temp);
            if(temp){
                x = i;
                y = j;
            }
        }
        arr.push_back(row);
    }
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            if(i - j == x - y and i != x and j != y or i + j == x + y and i != x and j != y) arr[i][j] = 2;
        }
    }
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            cout << arr[i][j] << " ";
        }
        cout << endl;
    }
    return 0;
}
