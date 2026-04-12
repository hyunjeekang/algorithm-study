#include <iostream>
using namespace std;

int gcd(int a, int b) {
    while (b > 0) {
        int temp = a % b;
        a = b;
        b = temp;
    }
    return a;
}
int main() {
    // Please write your code here.
    int n, m;
    cin >> n >> m;
    int r = gcd(n, m);
    int ans = r * (n / r) * (m / r);
    cout << ans;
    return 0;
}