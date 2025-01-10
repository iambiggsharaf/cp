#include <bits/stdc++.h>
using namespace std;
int main (){
    int n, cnt = 0;
    cin >> n;
    while(n){
        cnt++;
        n /= 10;
    }
    cout << cnt;
}
