#include <iostream>
#include <string>

using namespace std;

int main() {
    int N;
    cin >> N;
    int res = 0;
    res += N / 5 + N / 25 + N / 125;
    cout << res << '\n';

    return 0;
}