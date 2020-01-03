#include <iostream>
#include <vector>
#include <stack>
#include <queue>
#include <algorithm>


using namespace std;

class Node {
public:
    int num;
    bool visit;
    vector<int> adjacent;

    Node(int n) {
        num = n;
        visit = false;
    }
    void addAdjacent(int n) {
        adjacent.push_back(n);
    }
    void sortAdjacent() {
        sort(adjacent.begin(), adjacent.end());
    }
    bool isVisit() {
        return visit;
    }
    void setVisit(bool v) {
        visit = v;
    }
};

bool isAllVisited(vector<Node> graph) {
    for (int i = 0; i < graph.size(); i++) {
        if (!graph[i].isVisit()) {
            if (graph[i].adjacent.size() == 0) {
                continue ;
            } else {
                return false;
            }
        }
    }
    return true;
}



int main() {
    int N, M, V;
    cin >> N;
    cin >> M;
    cin >> V;
    vector<Node> graph;
    for (int i = 1; i <= N; i++) {
        Node tmp(i);
        graph.push_back(tmp);
    }
    int a, b;
    for (int i = 1; i <= M; i++) {
        cin >> a;
        cin >> b;
        graph[a - 1].addAdjacent(b);
        graph[b - 1].addAdjacent(a);
    }
    
    // DFS
    stack<int> s;
    s.push(V);
    graph[V - 1].setVisit(true);
    cout << V;
    while (!s.empty()) {
        int current = s.top();
		s.pop();
        graph[current - 1].sortAdjacent();
		for (int i = 0; i < graph[current - 1].adjacent.size(); i++) {

			int next = graph[current - 1].adjacent[i];

			if(!graph[next - 1].isVisit()){
				cout << ' ' << next;
				graph[next - 1].setVisit(true);
				s.push(current);
				s.push(next);
				break ;
			}
		}
    }
    cout << '\n';

    for (int i = 0; i < graph.size(); i++) {
        graph[i].setVisit(false);
    }
    // BFS
    queue<int> q;
    graph[V - 1].setVisit(true);
    q.push(V);
    int now;
    int tmpIdx;
    while (!isAllVisited(graph)) {
        if (graph[V - 1].adjacent.size() == 0) {
            break ;
        }
        now = q.front();
        q.pop();
        graph[now - 1].sortAdjacent();
        for (int i = 0; i < graph[now - 1].adjacent.size(); i++) {
            tmpIdx = graph[now - 1].adjacent[i];
            if (!graph[tmpIdx - 1].isVisit()) {
                q.push(tmpIdx);
                graph[tmpIdx - 1].setVisit(true);
            }
        }
        cout << now << ' ';
    }
    while (!q.empty()) {
        cout << q.front() << ' ';
        q.pop();
    }
    cout << '\n';

    return 0;
}