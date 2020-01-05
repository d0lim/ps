#include <iostream>
#include <vector>
#include <stack>
#include <algorithm>


using namespace std;

class Node {
private:
    int num;
    bool visit;
    int next;
public:
    Node(int n) {
        num = n;
        visit = false;
        next = 0;
    }
    int getNum() {
        return num;
    }
    void setNext(int _next) {
        next = _next;
    }
    int getNext() {
        return next;
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
    int T;
    cin >> T;
    
    for (int i = 1; i <= T; i++) {
        int N;
        cin >> N;
        vector<Node> graph;
        for (int j = 1; j <= N; j++) {
            int tmp;
            cin >> tmp;
            Node newNode(i);
            newNode.setNext(tmp);
            graph.push_back(newNode);
        }
        int count = 0;
        for (int j = 1; !isAllVisited(graph); j++) {
            if (graph[j - 1].isVisit()) {
                continue ;
            }
            int start = j;
            graph[j - 1].setVisit(true);
            for (int k = graph[j - 1].getNext(); k != start; k = graph[k - 1].getNext()) {
                graph[k - 1].setVisit(true);
            }
            count++;
        }
        cout << count << '\n';
    }
    
    return 0;
}