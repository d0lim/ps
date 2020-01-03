#include <iostream>

using namespace std;

int arr[1000001];

int main() {
    int N;
    cin >> N;
    for (int i = 1; i <= N; i++) {
        cin >> arr[i];
    }
    int max = -1000000;
    int min = 1000000;
    for (int i = 1; i <= N; i++) {
        if (max < arr[i]) {
            max = arr[i];
        }
        if (min > arr[i]) {
            min = arr[i];
        }
    }
    cout << min << ' ' << max << '\n';
    return 0;
}