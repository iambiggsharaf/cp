#include <bits/stdc++.h>
using namespace std;
int main (){
    int n = 10, m = 30, x, y, x1, y1, temp;
    cin >> x >> y >> x1 >> y1;
    vector < vector <int> > arr;
    for(int i = 0; i < n; i++){
        vector <int> row;
        for(int j = 0; j < m; j++){
            if(i == y and j >= x and j <= x1 or
                i == y1 and j >= x and j <= x1 or
                j == x and i >= y and i <= y1 or
                j == x1 and i >= y and i <= y1) row.push_back(1);
            else if(i > y and i < y1 and j > x and j < x1) row.push_back(2);
            else row.push_back(0);
        }
        arr.push_back(row);
    }
    for(auto row: arr){
        for(auto ele: row){
            cout << ele;
        }
        cout << "\n";
    }
}
