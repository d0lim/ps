#include <iostream>
#include <string>

using namespace std;

int classify(const char c) {
    if (c == ' ') {
        return 4;
    } else if (c >= 65 && c <= 90) {
        return 2;
    } else if (c >= 97 && c <= 122) {
        return 1;
    } else if (c >= 48 && c <= 57) {
        return 3;
    } else {
        return 0;
    }
}

int main() {
    for (int i = 0; i < 100; i++) {
        string input;
        int result[5] = { 0 };
        getline(cin, input);
        if (input == "")
            break;
        for (int j = 0; j < input.length(); j++) {
            result[classify(input[j])]++;
        }
        for (int j = 1; j <= 4; j++) {
            cout << result[j] << " ";
        }
        cout << endl;
    }
    return 0;
}