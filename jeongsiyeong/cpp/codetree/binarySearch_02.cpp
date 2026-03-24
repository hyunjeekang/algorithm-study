#include<iostream>
#include<vector>
using namespace std;

int N, M;
vector<pair<int, int>> number_with_cnt;

int bin_search(int m){
  int left = 0;
  int right = number_with_cnt.size() - 1;

  while (left<=right){
    int mid = (left + right) / 2;

    if (number_with_cnt[mid].first == m){
      return number_with_cnt[mid].second;
    }
    else if(number_with_cnt[mid].first < m){
      left = mid + 1;
    }
    else{
      right = mid - 1;
    }
  }
  return 0;
}

int main(){
    cin>>N>>M;

    vector<int> arr;
    for (int i=0; i<N; i++){
      int n;
      cin>>n;
      arr.push_back(n);
    }

    int cur_num=arr[0];
    int cur_cnt=1;

    for(int i=1; i<N; i++){
      if (arr[i] != cur_num){
        number_with_cnt.push_back({cur_num, cur_cnt});
        cur_num = arr[i];
        cur_cnt = 1;
      }
      else{
        cur_cnt++;
      }
    }

    number_with_cnt.push_back({cur_num, cur_cnt});

    for(int i=0; i<M; i++){
      int m;
      cin>>m;
      cout<<bin_search(m)<<"\n";
    }
}