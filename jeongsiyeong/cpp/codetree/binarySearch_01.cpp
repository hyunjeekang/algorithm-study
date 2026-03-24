#include<iostream>
#include<vector>
using namespace std;

int bin_search(int m, int N,const vector<int>& arr){
  int left = 0;
  int right = N - 1;

  while(left <= right){
    int mid = (left + right) / 2;

    if (arr[mid] == m){
      return mid+1;
    }
    else if (arr[mid] < m){
      left = mid + 1 ;
    }
    else{
      right = mid - 1;
    }
  }
  return -1;
}

int main(){
  int N, M ;

  cin >> N >> M;

  vector<int> arr;

  for(int i=0; i<N; i++){
    int n;
    cin>>n;
    arr.push_back(n);
  }

  for(int i=0; i<M; i++){
    int m;
    cin>>m;
    cout << bin_search(m, N , arr)<<"\n";
  }
}