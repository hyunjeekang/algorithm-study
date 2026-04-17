#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
    int N,M ;
    cin>>N>>M;

    vector<string> grid(N);
    for(int i=0; i<N; ++i){
        cin>>grid[i];
    }

    int max_sum =0;
    
    for (int mask=0; mask<(1<<N*M); ++mask){
        int cur_sum = 0;

        for(int r=0; r<N; ++r){
            int row_sum = 0;
            for(int c=0; c<M; ++c){
                int idx = r*M + c;

                if((mask & (1<<idx)) == 0){
                    row_sum = row_sum * 10 + (grid[r][c] - '0');
                }else{
                    cur_sum += row_sum;
                    row_sum=0;
                }

            }
            cur_sum += row_sum;
        }

        for(int c=0; c<M; ++c){
            int col_sum = 0;
            for(int r=0; r<N; ++r){
                int idx = r*M + c;

                if((mask & (1<<idx)) != 0){
                    col_sum = col_sum*10 + (grid[r][c] - '0');
                }else{
                    cur_sum += col_sum;
                    col_sum = 0;
                }

            }
            cur_sum += col_sum;
        }

        max_sum = max_sum > cur_sum ? max_sum: cur_sum;
    }
    cout<<max_sum;
}