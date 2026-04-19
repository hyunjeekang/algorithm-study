#include<iostream>
using namespace std;

int divide(int n, int r, int c){
  if (n==0)
    return 0;
  
  int half = 1 << (n-1);

  if (r< half && c<half){
    return divide(n-1, r, c);
  }
  else if(r<half && c>=half){
    return half*half + divide(n-1, r, c-half);
  }
  else if(r>=half && c<half){
    return 2*half*half + divide(n-1, r-half, c);
  }else{
    return 3*half*half + divide(n-1, r-half, c-half);
  }
}

int main(){
  int N, r, c;
  cin>>N>>r>>c;

  cout << divide(N, r, c) << "\n";
}