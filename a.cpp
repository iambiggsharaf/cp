#include <bits/stdc++.h>
using namespace std;
int main (){
    string s;
    cin >> s;
    for(auto i: s) cout << bitset<4>(stoi(string(1, i), nullptr, 16));
}
