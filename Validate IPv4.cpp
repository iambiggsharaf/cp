#include <bits/stdc++.h>
using namespace std;
int main() {
    string s, a, b, c, d;
    cin >> s;
    if(count(s.begin(), s.end(), '.') == 3){
        vector<int> pos{0};
        for(int i = 0; i < s.size(); i++) if(s[i] == '.') pos.push_back(i + 1);
        a = s.substr(0,pos[1] - 1);
        b = s.substr(pos[1], pos[2] - pos[1] - 1);
        c = s.substr(pos[2], pos[3] - pos[2] - 1);
        d = s.substr(pos[3], s.size() - pos[3]);
        try {cout << (stoi(a) >= 0 and stoi(b) >= 0 and
                       stoi(c) >= 0 and stoi(d) >= 0 and
                       stoi(a) <= 255 and stoi(b) <= 255 and
                       stoi(c) <= 255 and stoi(d) <= 255 ? "YES" : "NO");}
        catch(exception&e) {cout << "NO";}
    }
    else cout << "NO";
}
