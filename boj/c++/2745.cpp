#include <iostream>

using namespace std;

int translate(char c) {
    if (c >= '0' && c <= '9') {
        return (c - '0');
    } else {
        return (c - 55);
    }
}

int power(int B, int n) {
    int res = 1;
    for (int i = 0; i < n; i++) {
        res *= B;
    }
    return res;
}

int main() {
    string N;
    int B;
    cin >> N;
    cin >> B;
    int len = N.length();
    int res = 0;
    for (int i = 0; i < len; i++) {
        res += translate(N[i]) * power(B, len - i - 1);
    }
    cout << res << '\n';
    return 0;
}