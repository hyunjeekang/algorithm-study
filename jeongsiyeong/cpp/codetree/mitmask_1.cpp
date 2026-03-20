#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  int n;
  cin>>n;

  vector<int> arr(n);

  for (int i=0; i<n; i++){
    cin>>arr[i];
  }

  int answer = 0;

  for (int fir=0; fir<n; fir++){
    for(int sec=fir+1; sec<n; sec++){
      if((arr[fir] & arr[sec]) != 0){
        continue;
      }

      for(int thd = sec+1; thd<n; thd++){
        if(((arr[fir] | arr[sec]) & arr[thd]) == 0){
          answer = max(answer, arr[fir]+arr[sec]+arr[thd]);
        }
      }
    }
  }

  cout<<answer<<"\n";
}