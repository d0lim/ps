#include <iostream>
#include <cmath>

using namespace std;

bool prime[1000001];

void calculPrime(int start, int end) {
    bool tmp;
    for (int i = start; i <= end; i++) {
        tmp = true;
        if (i <= 1) {
            continue;
        }
        for (int j = 2; j <= sqrt(i); j++) {
            if (!prime[j]) {
                continue ;
            }
            else if (i % j == 0) {
                tmp = false;
                break ;
            }
        }
        if (tmp) {
            prime[i] = true;
        }
    }
}

int main() {
    ios_base :: sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int max = 1;

    int input;
    int tmp;
    bool done;
    while (true) {
        done = false;
        cin >> input;
        if (!input) {
            break ;
        }
        if (input > max) {
            calculPrime(max, input);
            max = input;
        }
        for (int i = 3; i <= input / 2; i++) {
            if (!prime[i]) {
                continue ;
            }
            tmp = input - i;
            if (prime[tmp]) {
                cout << input << " = " << i << " + " << tmp << '\n';
                done = true;
                break ;
            }
        }
        if (!done) {
            cout << "Goldbach's conjecture is wrong.\n";
        }
    }

    return 0;
}