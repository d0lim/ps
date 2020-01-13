#include <iostream>
#include <stdio.h>
#include <math.h>
#include <bitset>
#include <cstring>
#include <vector>
#include <queue>
#include <algorithm>
#define MAX 100001
#define INF 987654321
using namespace std;

int testcase;
int n,cnt;
int student[MAX];
bool visited[MAX];
bool finished[MAX];

void dfs(int now){
    visited[now] = true;
    
    int nxt = student[now];
    // 아직 방문하지 않은 경우
    if(!visited[nxt]){
        dfs(nxt);
    }
    // 이미 방문했던 경우
    // 1. 사이클 형성 도중 노드 방문 → 사이클 작업 수행
    // 2. 이미 앞에서 사이클 형성을 시도했던 노드 방문 → 아무 작업도 수행하지 않음
    else{
        // 1번 경우
        if(!finished[nxt]){
            // 만약 1 → 2 → 3 → 1 의 사이클이 형성되었다면
            // 1 부터 반복문을 돌린다 (now: 3, nxt: 1)
            // 사이클의 마지막 노드 전까지 반복하며 cnt++ 을 수행한다
            // 마지막 노드를 포함하면 곧바로 종료 되기 때문에 마지막에 cnt에 +1 을 수행해준다
            for(int i=nxt; i!=now; i=student[i]){
                cnt++;
            }
            cnt++;
        }
    }
    
    // 사이클 형성에 성공하거나 실패하였기 때문에 더이상 탐색 X
    finished[now] = true;
}

int main(int argc, const char * argv[]) {
    // cin,cout 속도향상
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    
    cin >> testcase;
    for(int t=0; t<testcase; t++){
        cin >> n;
        
        for(int i=1; i<=n; i++){
            cin >> student[i];
        }
        
        memset(visited, false, sizeof(visited));
        memset(finished, false, sizeof(finished));
        
        cnt = 0;
        for(int i=1; i<=n; i++){
            // 아직 방문하지 않은 경우
            if(!visited[i]){
                dfs(i);
            }
        }
        cout << n - cnt << "\n";
    }
}