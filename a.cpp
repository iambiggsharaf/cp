#include <bits/stdc++.h>
using namespace std;
int main (){
    string s;
    cin >> s;
    s = bitset<32>(stoll(s, nullptr, 2) - 1).to_string();
    try {cout << s.substr(s.find('1'));}
    catch(exception&e) {cout << 0;}
}
