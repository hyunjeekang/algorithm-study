#include<iostream>
#include<vector>
#include<string>
using namespace std;

vector<string>arr;

void inner_star(int r, int c, int n){
  if(n==3){
    arr[r][c] = '*';
    arr[r+1][c-1] = '*';
    arr[r+1][c+1] = '*';
    for (int i=c-2; i<=c+2; i++){
      arr[r+2][i] = '*';
    }
    return;
  }

  int half = n / 2;
  inner_star(r, c, half);
  inner_star(r+half, c-half, half);
  inner_star(r+half, c+half, half);
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  cout.tie(nullptr);
  
  int N;
  cin >>N;

  arr.assign(N, string(2*N-1,' '));

  inner_star(0, N-1, N);

  for(int i=0; i<N; ++i){
    cout<<arr[i]<<"\n";
  }

  return 0;
}