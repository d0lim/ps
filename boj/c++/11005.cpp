#include <iostream>
#include <stack>

using namespace std;

char translate(int num) {
    if (num < 10) {
        return (num + 48);
    } else {
        return (num + 55);
    }
}

int main() {
    stack<int> s;
    int N, B;
    cin >> N;
    cin >> B;

    while (N >= B) {
        s.push(N % B);
        N /= B;
    }
    s.push(N);
    int size = s.size();
    
    for (int i = 0; i < size; i++) {
        cout << translate(s.top());
        s.pop();
    }
    cout << '\n';

    return 0;
}