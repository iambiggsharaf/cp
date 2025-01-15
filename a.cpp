#include <bits/stdc++.h>
using namespace std;
int main (){
    string s;
    cin >> s;
    for(auto i: s) cout << bitset<3>(stoll(string(1, i), nullptr, 8)).to_string();
}
