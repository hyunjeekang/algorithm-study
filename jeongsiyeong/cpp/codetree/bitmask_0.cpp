#include<iostream>
#include<string>
using namespace std;

int main(){
  int q;
  cin>>q;
  
  int S = 0;

  for(int i= 0; i<q; ++i){
    string cmd;
    cin >> cmd;

    if (cmd == "clear"){
      S=0;
    }
    else{
      int x;
      cin>>x;
    
     if(cmd == "delete"){
      S &= ~(1<<x);
     }else if(cmd == "add"){
      S |= (1<<x);
     }else if(cmd == "print"){
      if(S& (1<<x)){
        cout<<1<<"\n";
      }else{
        cout<<0<<"\n";
      }
     }else if(cmd == "toggle"){
      S ^= (1<<x);
     }
    }
  }
  return 0;
}