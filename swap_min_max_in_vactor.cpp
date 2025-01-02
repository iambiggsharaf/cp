#include <bits/stdc++.h>
 using namespace std;
 int main (){
    int n, x, maxx, minn;
    cin >> n;
    vector <int> a;
    for(int i = 0; i < n; i++){
        cin >> x;
        a.push_back(x);
    }
    for(auto i: a){
        if(i == *max_element(a.begin(), a.end())) cout << *min_element(a.begin(), a.end()) << " ";
        else if(i == *min_element(a.begin(), a.end())) cout << *max_element(a.begin(), a.end()) << " ";
        else cout << i << " ";
    }
}
