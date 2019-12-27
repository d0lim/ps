#include <iostream>
#include <stack>

using namespace std;

int getPower(int b, int n) {
    int p = 1;
    for (int i = 1; i <= n; i++) {
        p *= b;
    }
    return p;
}

int main() {
    stack<int> s;
    int A, B;
    cin >> A;
    cin >> B;
    int m;
    cin >> m;
    int input = 0;
    int power = 1;
    int tmp;
    for (int i = m - 1; i >= 0; i--) {
        cin >> tmp;
        input += tmp * getPower(A, i);
    }
    while (input >= B) {
        s.push(input % B);
        input /= B;
    }
    s.push(input);
    int size = s.size();

    for (int i = 0; i < size; i++) {
        cout << s.top() << ' ';
        s.pop();
    }
    cout << '\n';
    

    return 0;
}