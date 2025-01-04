#include <bits/stdc++.h>
using namespace std;

int jam(int a, int b){

    int ans = a + b;
    return ans;
}

int main()
{
    int x, y;
    cin >> x >> y;
    int c = jam(x, y) * 2;
    cout << c;
}
