#include <iostream>
#include <queue>

using namespace std;

queue<int> q;

int main(void) {
	int N, K;
	cin >> N;
    cin >> K;
	for (int i = 1; i <= N; i++) {
		q.push(i);
	}
	cout << "<";
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < K - 1; j++) {
			q.push(q.front());
			q.pop();
		}
		if (i == N - 1) {
			cout << q.front() << ">\n";
			q.pop();
		}
		else {
			cout << q.front() << ", ";
			q.pop();
		}
	}
	return 0;
}
