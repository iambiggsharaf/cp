#include <bits/stdc++.h>
using namespace std;
int main() {
    string a, b;
    cin >> a >> b;
    cout << (stoll(a, nullptr, 2) >= stoll(b, nullptr, 2) ? a+"\n"+b : b+"\n"+a);
}
