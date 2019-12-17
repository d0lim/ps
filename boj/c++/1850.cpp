#include <iostream>

using namespace std;

long long gcd(long long a, long long b) {
    if (a < b) {
        long long tmp = a;
        a = b;
        b = tmp;
    }
    long long n = 0;
    while (b != 0) {
        n = a % b;
        a = b;
        b = n;
    }
    return a;
}

int main() {
    long long a, b;
    cin >> a;
    cin >> b;
    long long g = gcd(a, b);
    for (long long i = 0; i < g; i++) {
        cout << 1;
    }
    cout << '\n';
    return 0;
}
