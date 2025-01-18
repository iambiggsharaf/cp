#include <bits/stdc++.h>
using namespace std;
int main() {
    int x, y;
    cin >> x >> y;
    cout << ( (x <= 0 and y >= 0 and y <= (x + 7)) or (x >= 0 and y <= 0 and y >= (x + 7))  ? "Inside" : "Outside");
}
