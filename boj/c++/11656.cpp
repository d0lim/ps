#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

string suffixes[1001];

int main() {
    string input;
    cin >> input;

    int len = input.length();

    for (int i = 1; i <= len; i++) {
        suffixes[i] = input.substr(i - 1, len);
    }
    
    sort(suffixes + 1, suffixes + 1 + len);

    for (int i = 1; i <= len; i++) {
        cout << suffixes[i] << '\n';
    }

    return 0;
}
