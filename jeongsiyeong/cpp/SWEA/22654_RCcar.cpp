#include <iostream>
#include <vector>
#include <string>
using namespace std;
int N;
int dr[] = {-1, 0, 1, 0};
int dc[] = {0, 1, 0, -1};

bool is_range(int r, int c){
  return r>=0 && r<N && c>=0 && c<N;
}

int main()
{
  int T;
  cin >> T;
  for (int test_case = 1; test_case <= T; ++test_case)
  {
    cin >> N;
    vector<vector<char>> field(N, vector<char>(N, 'G'));

    int start_r = 0;
    int start_c = 0;
    int goal_r = 0;
    int goal_c = 0;
   

    for (int r = 0; r < N; r++)
    {
      for (int c = 0; c < N; c++)
      {
        cin >> field[r][c];
        if (field[r][c] == 'X')
        {
          start_r = r;
          start_c = c;
        }
        else if (field[r][c] == 'Y')
        {
          goal_r = r;
          goal_c = c;
        }
      }
    }
    
    int Q;
    cin>>Q;

    cout<<"#"<<test_case<<" ";
    for(int q=0; q<Q; q++){
      int dir = 0;
      int C;
      string cmd;

      cin>>C>>cmd;

      int cur_r = start_r;
      int cur_c = start_c;
      for(int i=0; i<C; i++){
        if(cmd[i] == 'A'){
          int nr = cur_r + dr[dir];
          int nc = cur_c + dc[dir];
          if(is_range(nr, nc) && field[nr][nc] != 'T'){
            cur_r = nr;
            cur_c = nc;
          }
        }
        else if(cmd[i] == 'R'){
          dir = (dir + 1) % 4;
        }
        else if(cmd[i] == 'L'){
          dir = (dir + 3) % 4;
        }
      }
      if (cur_r == goal_r && cur_c == goal_c){
        cout<<1<<" ";
      }
      else{
        cout<<0<<" ";
      }
    }
    cout<<"\n";
  }
}