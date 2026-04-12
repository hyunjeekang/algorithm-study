#include <iostream>
using namespace std;

int bitmap[62501] = {0};

void setBit(int val) {
    int n = val + 1000000;
    bitmap[n / 32] |= (1 << (n % 32));
}

bool getBit(int n) {
    return bitmap[n / 32] & (1 << (n % 32));
}

int main(){
  int n;
  cin >> n;
  
  for (int i= 0; i<n; i++){
    int val;
    cin>>val;
    setBit(val);
  }

  for(int i=2000000; i>=0; i--){
    if (getBit(i)){
      cout<<i - 1000000 << "\n";
    }
  }
}