#include <bits/stdc++.h>
using namespace std;
int main (){
    int n, a = 0, b = 0;
    cin >> n;
    while(n){
        if(n%10%2==0) a++;
        else b++;
        n/=10;
    }
    cout << a << " " << b;
}
