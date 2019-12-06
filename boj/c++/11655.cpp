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
    string input;
    getline(cin, input);
    for (int i = 0; i < input.length(); i++) {
        if (classify(input[i]) == 1) {
            int tmp = input[i];
            tmp += 13;
            if (tmp > 122)
                tmp -= 26;
            input[i] = tmp;
        } else if (classify(input[i]) == 2) {
            int tmp = input[i];
            tmp += 13;
            if (tmp > 90)
                tmp -= 26;
            input[i] = tmp;
        }
    }
    cout << input << endl;
    
    return 0;
}