#include <iostream>
#include <string>
#include <stack>

using namespace std;

stack<char> first;
stack<char> second;


bool edit(char command) {
    if (command == 'L') {
        if (!first.empty()) {
            second.push(first.top());
            first.pop();
        }
        return true;
    } else if (command == 'D') {
        if (!second.empty()) {
            first.push(second.top());
            second.pop();
        } 
        return true;
    } else if (command ==  'B') {
        if (!first.empty()) {
            first.pop();
        }
        return true;
    } else if (command == 'P') {
        char toAdd;
        cin >> toAdd;
        first.push(toAdd);
        return true;
    } else {
        return false;
    }
    return false;
}

int main() {
    string input;
    cin >> input;
    int N;
    cin >> N; 
    for (int i = 0; i < input.length(); i++) {
        first.push(input[i]);
    }
    char command;
    for (int i = 0; i < N; i++) {
        cin >> command;
        if (!edit(command))
            cout << "Error!!" << endl;
    }
    
    
    int outputLength = first.size() + second.size();
    char* output = new char[outputLength + 1]();
    int firstSize = first.size();
    for (int i = firstSize; i > 0; i--) {
        output[i - 1] = first.top();
        first.pop();
    }
    int secondSize = second.size();
    for (int i = 0; i < secondSize; i++) {
        output[i + firstSize] = second.top();
        second.pop();
    }
    cout << output << '\n';

    return 0;
}