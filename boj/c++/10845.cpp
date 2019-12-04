#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

int arr[10002];

int main() {
    int head = 1;
    int tail = 1;
    int N;

    cin >> N;

    for (int i = 1; i <= N; i++) {
        string command;
        cin >> command;
        if (command == "push") {
            int input;
            cin >> input;
            arr[tail] = input;
            tail++;
        } else if (command == "pop") {
            if (head != tail) {
                cout << arr[head] << '\n';
                head++;
            } else {
                cout << -1 << '\n';
            }
        } else if (command == "size") {
            cout << tail - head << '\n';
        } else if (command == "empty") {
            if (tail - head) {
                cout << 0 << '\n';
            } else {
                cout << 1 << '\n';
            }
        } else if (command == "front") {
            if (head != tail) {
                cout << arr[head] << '\n';
            } else {
                cout << -1 << '\n';
            }
        } else if (command == "back") {
            if (head != tail) {
                cout << arr[tail - 1] << '\n';
            } else {
                cout << -1 << '\n';
            }
        } else {
            cout << "Error\n";
        }
    }

    return 0;
}