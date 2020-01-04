#include <iostream>

using namespace std;

int main() {
    int max = 0;
    int idx = 0;
    int tmp;
    for (int i = 1; i <= 9; i++) {
        cin >> tmp;
        if (tmp > max) {
            idx = i;
            max = tmp;
        }
    }
    cout << max << '\n';
    cout << idx << '\n';
    
    return 0;
}