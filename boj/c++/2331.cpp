#include <iostream>
#include <string>
#include <cmath>

using namespace std;

int arr[10000001];

int main() {
    int A, P;
    cin >> A >> P;
    int tmp = A;
    int next = 0;
    while (true) {
        if (arr[tmp]) {
            break ;
        }
        next = 0;
        string s = to_string(tmp);
        for (int i = 0; i < s.length(); i++) {
            next += pow((s[i] - '0'), P);
        }
        arr[tmp] = next;
        tmp = next;
    }
    int count = 0;
    int tmp2 = A;
    while (true) {
        if (tmp == tmp2) {
            break ;
        }
        count++;
        tmp2 = arr[tmp2];
    }
    cout << count << '\n';

    return 0;
}
