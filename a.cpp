#include <bits/stdc++.h>
using namespace std;
int main() {
    string s;
    cin >> s;
    int cnt = 0;
    for(int i = 0; i < s.size(); i++){
        for(int j = 0; j < s.size(); j++){
            for(int k = 0; k < s.size(); k++){
                cout << cnt << ")\t" << s[i] << s[j] << s[k] << endl;
                cnt++;
            }
        }
    }
}
