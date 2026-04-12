#include<iostream>
using namespace std;

int total = 0;

void n_queen(int col, int ld, int rd, int chk){
  if (col == chk){
    total++;
    return;
  }

  int valid_positions = chk & (~(col | ld | rd));

  while(valid_positions != 0){
    int pos = valid_positions & -valid_positions;
    valid_positions -= pos;

    n_queen(col|pos, (ld|pos) << 1, (rd|pos) >> 1, chk);
  }
}

int main(){
  int N;

  cin >> N;

  int half = N / 2;

  int check = (1 << N) - 1;

  for(int i=0; i<half; i++){
    int pos = 1<<i;
    n_queen(pos, pos<<1, pos >> 1, check);
  }
  total *= 2;

  if (N%2 == 1){
    int pos = 1<<half;
    n_queen(pos, pos<<1, pos >> 1, check);
  }

  cout<<total<<"\n";
}

