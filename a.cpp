#include <bits/stdc++.h>
using namespace std;
int main(){
    double x, y;
    cin >> x >> y;
    bool big_circle = (pow(x,2) + pow(y,2) <= 25);
    bool small_a = (pow(x+1.5, 2) + pow(y-2, 2) < 1);
    bool small_b = (pow(x-1.5, 2) + pow(y-2, 2) < 1);
    bool semi = ((pow(x, 2) + pow(y, 2) < 9) and y < 0);
    bool teeth = (x >= -1 and x <= 1 and y >= -3 and y <= -2);

    if(big_circle and !small_a and !small_b and (!semi or teeth)){
        cout << "Inside";
    }
    else{
        cout << "Outside";
    }

}
