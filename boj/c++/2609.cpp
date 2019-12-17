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
    int a, b;
    cin >> a;
    cin >> b;

    int g = gcd(a, b);
    int l = a * b / g;
    cout << g << '\n';
    cout << l << '\n';

    return 0;
}
