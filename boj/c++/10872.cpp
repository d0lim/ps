#include <iostream>

using namespace std;

int main() {
    int N;
    cin >> N;
    int res = 1;
    for (int i = N; i >= 1; i--) {
        res *= i;
    }
    cout << res << '\n';
    return 0;
}