#include <iostream>
#include <algorithm>

using namespace std;
// nCm = n! / m!*(n-m)!
int numOf2(int n) { 
    int val = n;
    int count = 0;
    while (val > 0) {
        val /= 2;
        count += val;
    }
    return count;
}

int numOf5(int n) {
    int val = n;
    int count = 0;
    while (val > 0) {
        val /= 5;
        count += val;
    }
    return count;
}

int main() {
    int n, m;
    cin >> n;
    cin >> m;
    int num5 = numOf5(n) - numOf5(m) - numOf5(n - m);
    int num2 = numOf2(n) - numOf2(m) - numOf2(n - m);
    cout << min(num5, num2) << '\n';

    return 0;
}