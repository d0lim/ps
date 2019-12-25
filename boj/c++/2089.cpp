#include <iostream>
#include <stack>

using namespace std;

int main(){
	int num;
	cin >> num;
	stack<int> S;

	do {
		int left = num % -2;
		num = num / -2;
		
		if(left < 0){
			left = 1;
			num++;
		}
		S.push(left);
	} while (num != 0);

	while (!S.empty()){
		cout << S.top();
		S.pop();
	}
	cout << '\n';
}
