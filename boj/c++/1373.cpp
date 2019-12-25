#include <iostream>
#include <string>
#include <stack>

using namespace std;

int main() {
    stack<int> s;
    string N;
    cin >> N;
    int len = N.length();
    int i;
    for (i = len - 1; i > 1; i -= 3) {
        s.push((N[i] - '0') + (N[i - 1] - '0') * 2 + (N[i - 2] - '0') * 4);
    };
    if (i == 0) {
        s.push((N[0] - '0'));
    } else if (i == 1) {
        s.push((N[0] - '0') * 2 + (N[1] - '0'));
    }
    len = s.size();
    for (i = 0; i < len; i++) {
        cout << s.top();
        s.pop();
    }
    cout << '\n';

    return 0;
}