#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;

struct MyString{
  string value;

  bool operator<(const MyString& other) const{
    if (this->value.length() != other.value.length()){
      return this->value.length() < other.value.length();
    }
    return this->value < other.value;
  }

  bool operator==(const MyString& other) const{
    return this->value == other.value;
  }
};

int main(){
  vector<MyString> list;

  int N;
  cin>>N;

  for (int i=0; i<N; i++){
    string s;
    cin>>s;
    list.push_back({move(s)});
  }

  sort(list.begin(), list.end());

  list.erase(unique(list.begin(), list.end()), list.end());

  for(const auto& s : list){
    cout<<s.value<<"\n";
  }

  return 0;
}