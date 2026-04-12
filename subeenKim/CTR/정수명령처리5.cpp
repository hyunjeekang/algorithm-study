#include <iostream>
#include <vector>
using namespace std;

int main() {
    // Please write your code here.
    vector <int> v;
    int N;
    cin >> N;
    for (int i = 0;i < N;i++) {
        string command;
        cin >> command;
        if (command == "size") {
            cout << v.size() << endl;
        }
        else if (command == "pop_back") {
            v.pop_back();
        }
        else {
            int num;
            cin >> num;
            if (command == "push_back") {
                v.push_back(num);
            }
            else {
                cout << v[num - 1] << endl;
            }
        }
    }
    return 0;
}