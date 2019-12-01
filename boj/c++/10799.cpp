#include <iostream>
#include <algorithm>
#include <string>
#include <stack>

using namespace std;

int main() {
    string input;
    cin >> input;
    
    stack<char> st;
    int count = 0;

    for (int i = 0; i < input.size(); i++) {
        if (input[i] == '(') 
            st.push(input[i]);
        else {
            st.pop();
            if (input[i - 1] == '(')
                count += st.size();
            else
                count++;
        }
    }

    cout << count << endl;
    
    return 0;
}