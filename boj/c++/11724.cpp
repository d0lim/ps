#include <iostream>
#include <vector>
#include <stack>
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
            return false;
        }
    }
    return true;
}

int main() {
    int N, M;
    cin >> N;
    cin >> M;

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
    int count = 0;
    for (int j = 1; !isAllVisited(graph); j++) {
        if (graph[j - 1].isVisit()) {
            continue ;
        }
        stack<int> s;
        s.push(j);
        graph[j - 1].setVisit(true);
        while (!s.empty()) {
            int current = s.top();
            s.pop();
            graph[current - 1].sortAdjacent();
            for (int i = 0; i < graph[current - 1].adjacent.size(); i++) {

                int next = graph[current - 1].adjacent[i];

                if(!graph[next - 1].isVisit()){
                    graph[next - 1].setVisit(true);
                    s.push(current);
                    s.push(next);
                    break ;
                }
            }
        }
        count++;
    }
    
    cout << count << endl;
    
    return 0;
}