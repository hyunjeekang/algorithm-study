#include <iostream>
#include <vector>
using namespace std;

int main() {
    // Please write your code here.
    int N1, N2;
    cin >> N1 >> N2;
    vector<int> A(N1);
    vector<int> B(N2);
    for (int i=0;i<N1;i++){
        cin >> A[i];
    }
    for (int i=0;i<N2;i++){
        cin >> B[i];
    }

    bool is_found = false, is_find_all = false;
    for (int i=0; i<N1;i++){
        if (A[i] == B[0]){
            int a = i;
            for (int b=0;b<N2;b++){
                if (a >= N1){
                    break;
                }
                if (B[b] != A[a]){
                    break;
                }
                a++;
                if (b==N2-1){
                    is_find_all = true;
                    cout << "Yes";
                    break;
                }
            }
        }
        if (is_find_all){
            break;
        }
    }

    if (!is_find_all){
        cout << "No";
    }
    return 0;
}