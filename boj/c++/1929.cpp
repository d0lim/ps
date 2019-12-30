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
    int M, N;
    cin >> M;
    cin >> N;
    calculPrime(1, M);
    calculPrime(M, N);
    
    for (int i = M; i <= N; i++) {
        if (prime[i]) {
            cout << i << '\n';
        }
    }

    return 0;
}