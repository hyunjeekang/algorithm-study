#include <iostream>
#include <vector>
using namespace std;

int main() {
    // Please write your code here.
    int N, M;
    cin >> N >> M;
    vector<vector<int>> grid1(N, vector<int>(M));
    vector<vector<int>> grid2(N, vector<int>(M));
    for(int i=0;i<N;i++){
        for(int j=0;j<M;j++){
            cin >> grid1[i][j];
        }
    }

    for(int i=0;i<N;i++){
        for(int j=0;j<M;j++){
            cin >> grid2[i][j];
        }
    }

    for(int i=0;i<N;i++){
        for(int j=0;j<M;j++){
            if (grid1[i][j] == grid2[i][j]){
                cout << "0" << " ";
            }
            else {
                cout << "1" << " ";
            }
        }
        cout << endl;
    }
    return 0;
}