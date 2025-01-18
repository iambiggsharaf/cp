#include <bits/stdc++.h>
using namespace std;
int main() {
    int x, y;
    cin >> x >> y;
    cout << ((x <= -5) or (x >= -2 and x <= 3 and y >= 3) or (x >= 6) ? "Inside" : "Outside");
}
