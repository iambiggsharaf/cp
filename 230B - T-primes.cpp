#include <bits/stdc++.h>
using namespace std;
bool isPrime(long long n) {
    if (n <= 1) return false; // Numbers <= 1 are not prime
    if (n <= 3) return true;  // 2 and 3 are prime
    if (n % 2 == 0 || n % 3 == 0) return false; // Eliminate multiples of 2 and 3

    // Check divisors from 5 to sqrt(n) using the 6k ± 1 optimization
    for (long long i = 5; i * i <= n; i += 6) {
        if (n % i == 0 || n % (i + 2) == 0) return false;
    }
    return true; // Prime if no divisors found
}
int main() {
    long long n, a;
    cin >> n;
    while(n--){
        cin >> a;
        cout << ( pow(int(sqrt(a)), 2) == a and isPrime(int(sqrt(a))) ? "YES\n" : "NO\n");
    }
}
