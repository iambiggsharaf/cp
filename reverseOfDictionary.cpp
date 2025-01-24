#include <bits/stdc++.h>
using namespace std;
int main(){
    int n;
    string s;
    cin >> n;
    cin.ignore();
    map <string, vector<string>> dict;
    for(int i = 0; i < n; i++){
        getline(cin, s);
        string key = s.substr(0, s.find('-') - 1);
        string words1 = s.substr(s.find('-') + 1, s.size() - s.find('-') - 1);
//        cout << key << words1 << endl;
        stringstream words(words1);
        std::string item;
        while (std::getline(words, item, ',')) {
            item.erase(0, item.find_first_not_of(" \t"));
            item.erase(item.find_last_not_of(" \t") + 1);
            dict[item].push_back(key);
        }
    }
    cout << dict.size() << endl;
    for(auto i: dict){
        cout << i.first << " - ";
        for(int j = 0; j < i.second.size(); j++)
        {
            if(j == i.second.size() - 1) cout << i.second[j] << "\n";
            else cout << i.second[j] << ", ";
        }
    }
}

