#include <bits/stdc++.h>
using namespace std;
int main() {
    int n;
    cin >> n;
    string s = bitset<32>(n).to_string();
    reverse(s.begin(), s.end());
    cout << stoi(s, nullptr, 2);
}
