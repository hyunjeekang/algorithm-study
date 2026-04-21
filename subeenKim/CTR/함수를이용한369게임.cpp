#include <iostream>
#include <string>
using namespace std;
int a, b;

bool one_of_369(int i){
    string num = to_string(i);
    for (char c:num){
        if(c=='3' || c=='6' || c=='9'){
            return true;
        }
    }
    return false;
}

bool multiple_of_3(int i){
    return (i%3==0);
}
int main() {
    cin >> a >> b;
    int cnt = 0;
    for (int i=a;i<=b;i++){
        if (one_of_369(i) || multiple_of_3(i)){
            cnt++;
        }
    }
    cout << cnt;
    return 0;
}