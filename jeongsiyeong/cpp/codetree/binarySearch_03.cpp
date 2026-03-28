#include <iostream>
#include <vector>

using namespace std;

int n,m;
vector<int> arr;
vector<int> querys;

int bin_search(int q){
  int left = 0;
  int right = n -1;
  int answer = -1;

  while(left <= right){
    int mid = left + (right - left ) / 2;

    if (arr[mid] == q){
      answer = mid + 1;
      right = mid - 1;
    }else if (arr[mid] < q){
      left = mid + 1;
    }else{
      right = mid - 1;
    }
  }
  return answer;
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  arr.resize(n);
  for(int i=0; i<n; i++){
    cin >> arr[i];
  }

  querys.resize(m);
  for(int i=0; i<m; i++){
    cin >> querys[i];
  }

  for(int i=0; i<m; i++){
    cout<<bin_search(querys[i]) <<"\n";
  }
}