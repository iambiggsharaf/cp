#include <bits/stdc++.h>
using namespace std;
int main (){
    string s;
    cin >> s;
    for(int i = 0; i < s.size(); i+=4){
        cout << uppercase << hex << stoll(s.substr(i, 4), nullptr, 2);
    }
}
