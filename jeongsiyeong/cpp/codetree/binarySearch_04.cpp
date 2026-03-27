#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int n,m;
vector<int> arr;

int upper_bound(int target){
  int left = 0;
  int right = 0;
  int min_idx = n;

  while(left <= right){
    int mid = (left + right) / 2;

    if (arr[mid] > target){
      right = mid - 1;
      min_idx = min(min_idx, mid);

    }else{
      left = mid + 1;
    }

  }

  return min_idx;
}

int lower_bound(int target){
  int left = 0;
  int right = 0;
  int min_idx = n;

  while(left <= right){
    int mid = (left + right) / 2;

    if (arr[mid] >= target){
      right = mid - 1;
      min_idx = min(min_idx, mid);

    }else{
      left = mid + 1;
    }

  }

  return min_idx;
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  arr.resize(n);
  for(int i = 0; i<n; i++){
    cin >> arr[i];
  }

  sort(arr.begin(), arr.end());

  for(int i=0; i<m; i++){
    int a,b;

    cin>>a>>b;
    int count = upper_bound(b) - lower_bound(a);
    cout<<count<<"\n";
  }
}