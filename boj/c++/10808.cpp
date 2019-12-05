#include <iostream>
#include <string>

using namespace std;

int arr[28];

int main() {
    string input;
    cin >> input;
    for (int i = 0; i < input.length(); i++) {
        arr[input[i] - 96]++;
    }
    for (int i = 1; i <= 25; i++) {
        cout << arr[i] << " ";
    }
    cout << arr[26] << '\n';

    return 0;
}