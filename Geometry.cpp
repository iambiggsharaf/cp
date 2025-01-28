#include <bits/stdc++.h>
using namespace std;
int main() {
    double x, y;
    cin >> x >> y;
    bool a = ((pow(x,2) + pow(y, 2)) <= 36);
    bool b = ((pow(x-0,2) + pow(y+3, 2)) < 4);
    bool c = ((pow(x+2,2) + pow(y-2, 2)) < 1);
    bool d = ((pow(x-2,2) + pow(y-2, 2)) < 1);
//    bool e = (x >= -3 and x <= 3 and y <= 3 and y>=-3);
    if(a and !b and !c and !d) cout << "Inside";
    else cout << "Outside";
}
