#include <iostream>
#include <string>

using namespace std;

int main() {
    string A, B, C, D;
    cin >> A;
    cin >> B;
    cin >> C;
    cin >> D;
    string first = A + B;
    string second = C + D;

    cout << stol(first) + stol(second) << endl;

    return 0;
}