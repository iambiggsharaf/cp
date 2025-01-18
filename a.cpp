#include <bits/stdc++.h>
using namespace std;
int main() {
    int x, y;
    cin >> x >> y;
    cout << ( (y <= 3 and x <= 3 and y >= (-x-4)) and !( y <= 1 and x <= 1 and y >= (-x-2) )  ? "Inside" : "Outside");
}
