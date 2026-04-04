#include <iostream>
#include <string>
#include <stack>

using namespace std;

string str;

int main() {
    cin >> str;

    // Please write your code here.
    bool is_yes = true;
    stack <int> st;
    for (char c : str) {
        if (c == '(') {
            st.push(c);
        }
        else {
            if (st.empty() == false && st.top() == '(') {
                st.pop();
            }
            else {
                is_yes = false;
                break;
            }
        }
    }
    if (st.empty() && is_yes) {
        cout << "Yes";
    }
    else {
        cout << "No";
    }
    return 0;
}
