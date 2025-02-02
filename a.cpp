#include <bits/stdc++.h>
using namespace std;
int main(){
    double x, y;
    cin >> x >> y;
    bool a = (pow(x-5, 2) + pow(y, 2) <= 4 and y <= 0);

    bool b = (pow(x, 2) + pow(y-3, 2) < 1);

    bool c = (y <= 5);
    bool d = (y >= -8*x/3-3);
    bool e = (y >= 8*x/3-3);
    cout << ( (a) or (c and d and e and !b) ? "Inside" : "Outside");
}
