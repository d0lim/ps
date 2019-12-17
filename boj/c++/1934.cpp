#include <iostream>

using namespace std;

int gcd(int a, int b) {
    if (a < b) {
        int tmp = a;
        a = b;
        b = tmp;
    }
    int n = 0;
    while (b != 0) {
        n = a % b;
        a = b;
        b = n;
    }
    return a;
}

int main() {
    int T;
    cin >> T;
    int a, b;
    int l;
    for (int i = 1; i <= T; i++) {
        cin >> a;
        cin >> b;
        l = a * b / gcd(a, b);
        cout << l << '\n';
    }
    return 0;
}
