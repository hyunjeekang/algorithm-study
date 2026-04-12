#include <string>
#include <vector>

using namespace std;

int gcd(int n, int m) {
    while (m > 0) {
        int r = n % m;
        n = m;
        m = r;
    }
    return n;
}

vector<int> solution(int numer1, int denom1, int numer2, int denom2) {
    vector<int> answer;
    int denom = denom1 * denom2;
    int numer = denom2 * numer1 + denom1 * numer2;
    int num = gcd(numer, denom);
    answer.push_back(numer / num);
    answer.push_back(denom / num);
    return answer;
}