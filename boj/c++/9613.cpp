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

long long input[101];

int main() {
    int t;
    int n;
    long long sum = 0;

    cin >> t;
    for (int i = 1; i <= t; i++) {
        sum = 0;
        cin >> n;
        for (int j = 1; j <= n; j++) {
            cin >> input[j];
        }
        for (int j = 1; j < n; j++) {
            for (int k = j + 1; k <= n; k++) {
                sum += gcd(input[j], input[k]);
            }
        }
        cout << sum << '\n';
    }
    return 0;
}
