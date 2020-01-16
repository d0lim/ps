#include <iostream>
#include <queue>
#include <vector>
#include <utility>
#include <algorithm>

using namespace std;

int arr[26][26];

// int flatten(int N, int x, int y) {
//     return (N * x + y);
// }

// int parseX(int N, int flat) {
//     return (flat / N);
// }

// int parseY(int N, int flat) {
//     return (flat % N);
// }

int bfs(int N, int start_x, int start_y) {
    // cout << "BFS started!" << endl;
    int count = 0;
    queue<pair<int, int>> q;
    q.push(pair<int, int>(start_x, start_y));
    arr[start_x][start_y] = -1;
    while (!q.empty()) {
        int x = q.front().first;
        int y = q.front().second;
        q.pop();
        // cout << "Visited [" << x << "][" << y << "]\n";
        count++;
        if (arr[x - 1][y] == 1) {
            q.push(pair<int, int>(x - 1, y));
            arr[x - 1][y] = -1;
        }
        if (arr[x][y - 1] == 1) {
            q.push(pair<int, int>(x, y - 1));
            arr[x][y - 1] = -1;
        }
        if (arr[x + 1][y] == 1) {
            q.push(pair<int, int>(x + 1, y));
            arr[x + 1][y] = -1;
        }
        if (arr[x][y + 1] == 1) {
            q.push(pair<int, int>(x, y + 1));
            arr[x][y + 1] = -1;
        }
    }
    return count;
}

int main() {
    ios_base :: sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    int N;
    cin >> N;
    
    for (int i = 1; i <= N; i++) {
        string line;
        cin >> line;
        for (int j = 0; j < N; j++) {
            arr[i][j + 1] = line[j] - '0';
        }
    }
    // cout << "Input ended" << endl;
    // for (int i = 1; i <= N; i++) {
    //     for (int j = 1; j <= N; j++) {
    //         cout << arr[i][j];
    //     }
    //     cout << endl;
    // }
    int complex = 0;
    vector<int> countInComplex;
    for (int i = 1; i <= N; i++) {
        for (int j = 1; j <= N; j++) {
            if (arr[i][j] == 1) {
                countInComplex.push_back(bfs(N, i, j));
                complex++;
            }
        }
    }
    sort(countInComplex.begin(), countInComplex.end());
    cout << complex << '\n';
    for (int i = 0; i < countInComplex.size(); i++) {
        cout << countInComplex[i] << '\n';
    }

    return 0;
}