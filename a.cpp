#include <bits/stdc++.h>
using namespace std;
int main() {
    int x, y;
    cin >> x >> y;
    cout << (y <= (x + 6) and y >= (x - 3) and y <= (-x + 5) and y >= (-x - 7)  ? "Inside" : "Outside");
}
