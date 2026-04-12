#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int higher(int a, int b){
  if (a>b){
    return 1;
  }
  return 0;
}

int main(){
  ios_base::sync_with_stdio
  int T;
  cin>>T;

  for (int test_case = 1; test_case <= T; ++test_case){
    int N;
    cin>>N;

    vector<vector<int>> arr(N);

    for (int r=0; r<N; r++){
      for(int c=0; c<N; c++){
        int a;
        cin>>a;
        arr[r].push_back(a);
      }
    }

    vector<vector<int>> dp(N, vector<int>(N,0));

    for (int i=1; i<N; i++){
      dp[i][0] = dp[i-1][0] + higher(arr[i][0], arr[i-1][0]) + 1;
      dp[0][i] = dp[0][i-1] + higher(arr[0][i], arr[0][i-1]) + 1;
    }
  
    for(int r=1; r<N; r++){
      for(int c=1; c<N; c++){
        int down = dp[r-1][c] + higher(arr[r][c], arr[r-1][c]) + 1;
        int right = dp[r][c-1] + higher(arr[r][c], arr[r][c-1]) + 1;
        dp[r][c] = min(down, right);
      }
    }

    cout<<'#'<<test_case<<dp[N-1][N-1]<<"\n";
  }
}