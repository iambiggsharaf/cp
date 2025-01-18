#include <bits/stdc++.h>
using namespace std;
int main() {
    int x, y;
    cin >> x >> y;
    cout << ((y >= (x - 5) and (y >= (-x-2))) ? "Inside" : "Outside");
}
