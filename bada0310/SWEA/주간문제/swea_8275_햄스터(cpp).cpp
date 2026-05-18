#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// 선언부 
int N, X, M;
vector<vector<int>> arr;
vector<int> res;
vector<vector<int>> results;
// 함수 정의 부 
bool check(int i, int r, int cnt, const std::vector<int>& res){
  int c = 0;

  for (int idx = i-1; idx < r; ++idx){
    c += res[idx];
  }

  if (c == cnt){
    return true;
  }
  return false;
};

// std::vector<std::vector< tuple<int,int,int>>>
void cnt_hamster(int depth){
  if (depth == N){
    bool is_ok = true;
    // vector<vector<int>>
    for (const auto& condition : arr){
      int i = condition[0];
      int r = condition[1];
      int cnt = condition[2];

      if (!check(i, r, cnt, res)){
        is_ok = false;
        break;
      }
    }
    if (is_ok){
      results.push_back(res);
    }
    return;
  }

  for (int num = 0; num < X+1; num+=1){
    res.push_back(num);
    cnt_hamster(depth+=1);
    res.pop_back(); //
  }
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int T;
    cin >> T; 

    // 수정: 이 중괄호가 끝나는 시점은 결과 출력 후(가장 아래)여야 합니다!
    for(int tc = 1; tc <= T; ++tc){
        cin >> N >> X >> M;
        
        arr.clear();
        res.clear();
        results.clear();

        for(int m = 0; m < M; ++m){
            int i, r, cnt;
            cin >> i >> r >> cnt;
            // 수정: 끝에 세미콜론(;) 추가
            arr.push_back({i, r, cnt}); 
        }
        
        cnt_hamster(0);
        
        // 결과 처리 
        if(!results.empty()){
            int max_sum = -1;
            
            // 1. 최대합 구하기
            for (const auto& r: results){
                int curr_sum = 0; // 수정: 여기서 0으로 초기화
                for (int val : r){
                    curr_sum += val; // 수정: 더하기 대입 연산자
                }
                if (curr_sum > max_sum){
                    max_sum = curr_sum;
                }
            }
            
            vector<vector<int>> ans;
            // 2. 미완성되었던 ans에 담는 부분 완성
            for (const auto& r: results){
                int curr_sum = 0;
                for (int val : r) curr_sum += val;
                
                if (curr_sum == max_sum) { // 방금 구한 합이 최대합과 같다면
                    ans.push_back(r);      // 정답 리스트에 추가
                }
            }

            sort(ans.begin(), ans.end()); 

            cout << "#" << tc << " ";
            for (int val : ans[0]){
                cout << val << " ";
            }
            cout << '\n';
        } else {
            // 수정: -1 앞에 띄어쓰기 추가 (" -1\n")
            cout << "#" << tc << " -1\n"; 
        }
    } // 테스트 케이스 반복문 종료

    // 수정: return 0은 main 함수의 중괄호 안에 있어야 함
    return 0; 
}
// ___________________________________________

#include <iostream>
#include <vector>
#include <algorithm> // sort() 사용을 위해 필요

using namespace std;

// 전역 변수 선언 (파이썬의 global 역할)
int N, X, M;
vector<vector<int>> arr;
vector<int> res;
vector<vector<int>> results;

// 조건에 맞는지 확인하는 함수  
bool check(int i, int r, int cnt, const vector<int>& res) {
    int c = 0;
    // 파이썬: for idx in range(i-1, r):
    for (int idx = i - 1; idx < r; ++idx) {
        c += res[idx];
    }
    
    if (c == cnt) {
        return true;
    }
    return false;
}

// 중복 순열의 목적: 모든 경우의 수를 탐색하면서 선택(push_back) 와 취소(pop_back)
void cnt_hamster(int depth) { 
    if (depth == N) {
        bool is_ok = true;
        // 파이썬: for condition in arr:
        for (const auto& condition : arr) {
            int i = condition[0];
            int r = condition[1];
            int cnt = condition[2];
            
            // 조건에 부합하는지 확인
            if (!check(i, r, cnt, res)) {
                is_ok = false; // 적합하지 않은 조건이 있다. 
                break;
            }
        }
        
        // flag 가 다 체크되고 나면
        if (is_ok) {
            results.push_back(res); // 파이썬의 results.append(list(res))
        }
        return;
    }

    // 파이썬: for num in range(X+1):
    for (int num = 0; num <= X; ++num) {
        res.push_back(num);       // append
        cnt_hamster(depth + 1);   // 다음 깊이로
        res.pop_back();           // pop
    }
}

int main() {
    // 입출력 속도 향상
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int T;
    if (!(cin >> T)) return 0; // T = int(input())

    // 파이썬: for tc in range(1, T+1):
    for (int tc = 1; tc <= T; ++tc) {
        // N, X, M = map(int, input().split())
        cin >> N >> X >> M;

        // 매 테스트 케이스마다 전역 변수 초기화
        arr.clear();
        res.clear();
        results.clear();

        // 파이썬: for _ in range(M):
        for (int m = 0; m < M; ++m) {
            int i, r, cnt;
            cin >> i >> r >> cnt; // i, r, cnt = map(int, input().split())
            arr.push_back({i, r, cnt}); // arr.append((i, r, cnt))
        }

        cnt_hamster(0);

        // 파이썬: if len(results) >= 1:
        if (!results.empty()) { 
            
            // 1. max_sum 구하기
            int max_sum = -1;
            for (const auto& r_vec : results) {
                int current_sum = 0;
                for (int val : r_vec) {
                    current_sum += val;
                }
                if (current_sum > max_sum) {
                    max_sum = current_sum;
                }
            }

            // 2. 최대 합을 가진 결과만 ans에 저장
            vector<vector<int>> ans;
            for (const auto& r_vec : results) {
                int current_sum = 0;
                for (int val : r_vec) {
                    current_sum += val;
                }
                if (current_sum == max_sum) {
                    ans.push_back(r_vec);
                }
            }

            // 파이썬: ans.sort() (사전 순으로 정렬)
            sort(ans.begin(), ans.end());

            // 파이썬: print(f'#{tc}', *ans[0])
            cout << "#" << tc << " ";
            for (int val : ans[0]) {
                cout << val << " ";
            }
            cout << "\n";
            
        } else {
            // 파이썬: print(f'#{tc}', -1)
            cout << "#" << tc << " -1\n";
        }
    }

    return 0;
}