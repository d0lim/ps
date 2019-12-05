#include <iostream>
#include <string>

using namespace std;

int arr[28];

int main() {
    string input;
    cin >> input;
    for (int i = 97; i <= 122; i++) {
        arr[i - 96] = -1;
        for (int j = 0; j < input.length(); j++) {
            if ((int)input[j] == i) {
                arr[i - 96] = j;
                break;
            }
        }
    }
    for (int i = 1; i <= 25; i++) {
        cout << arr[i] << " ";
    }
    cout << arr[26] << '\n';

    return 0;
}