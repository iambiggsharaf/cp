#include <bits/stdc++.h>
using namespace std;
int main (){
    string s;
    int cnt = 0;
    cin >> s;
    for(int i = 0; i < s.size(); i+=3){
        cout << stoi(s.substr(i, 3), nullptr, 2);
    }
}
