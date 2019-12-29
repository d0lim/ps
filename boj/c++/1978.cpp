#include <iostream>

using namespace std;

bool prime[1001];
int input[101];

void calculPrime(int start, int end) {
    bool tmp;
    for (int i = start; i <= end; i++) {
        tmp = true;
        if (i <= 1) {
            continue;
        }
        for (int j = 2; j < i; j++) {
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
    int N;
    cin >> N;
    int tmp;
    int max = 0;
    for (int i = 1; i <= N; i++) {
        cin >> tmp;
        input[i] = tmp;
        if (tmp > max) {
            calculPrime(max, tmp);
            max = tmp;
        }
    }
    int count = 0;
    for (int i = 1; i <= N; i++) {
        if (prime[input[i]]) {
            count++;
        }
    }
    cout << count << '\n';

    return 0;
}