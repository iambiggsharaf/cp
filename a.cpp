#include <bits/stdc++.h>
using namespace std;
int main (){
    int n, a = 0, b = 0;
    while(cin >> n){
        if(n == 0) break;
        if(n % 6 == 0 and n % 10 == 4) a+=n;
    }
    cout << a;
}
