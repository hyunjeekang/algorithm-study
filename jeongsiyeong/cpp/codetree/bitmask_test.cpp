#include<iostream>
#include<vector>
using namespace std;

int main(){
  int n;
  cin>>n;

  vector<int> arr(n);

  for(int i=0; i<n; i++){
    int c;
    cin>>c;
    int tmp=0;

    for(int j=0; j<c; j++){
      int t;
      cin>>t;
      tmp |= (1<<t);
    }
    arr[i] = tmp;
  }
  int cnt=0;
  for(int fir=0; fir < n; fir++){
    for(int sec=fir+1; sec<n; sec++){
      if((arr[fir]+arr[sec]) == (arr[fir]|arr[sec])){
        cnt++;
      }
    }
  }
  cout<<cnt<<"\n";
}