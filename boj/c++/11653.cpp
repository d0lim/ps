#include <iostream>

using namespace std;

int main() {
    ios_base :: sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int N;
    cin >> N;
    for (int i = 2; i <= N;) {
        if (N % i == 0) {
            cout << i << '\n';
            N /= i;
        } else {
            i++;
        }
    }
    return 0;
}