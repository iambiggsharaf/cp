#include <bits/stdc++.h>
using namespace std;
int main() {
    int n;
    string a, b;
    cin >> n;
    map <string, string> dict;
    while(n--){
        cin >> a >> b;
        dict[a] = b;
        dict[b] = a;
    }
    cin >> a;
    cout << dict[a];
}
