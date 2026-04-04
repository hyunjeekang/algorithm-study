#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int x1, y1, x2, y2, x3, y3, x4, y4;
    cin >> x1 >> y1 >> x2 >> y2;
    cin >> x3 >> y3 >> x4 >> y4;

    int r1 = max(x1, x3);
    int r2 = min(x2, x4);
    int c1 = max(y1, y3);
    int c2 = min(y2, y4);

    int ans;
    if (r1 >= r2 || c1 >= c2) {
        ans = (x2 - x1) * (y2 - y1);
    }
    else if (x3 <= x1 && x2 <= x4 && y3 <= y1 && y2 <= y4) {
        ans = 0;
    }
    // 2. 세로 변 전체를 덮어 가로 길이만 줄어드는 경우
    else if ((x3 <= x1 && x2 <= x4) && ((y1 < y3 && y2 <= y4) || (y2 > y4 && y3 <= y1))) {
        ans = (x2 - x1) * ((y2 - y1) - (c2 - c1));
    }
    // 3. 가로 변 전체를 덮어 세로 길이만 줄어드는 경우
    else if ((y3 <= y1 && y2 <= y4) && ((x1 < x3 && x2 <= x4) || (x2 > x4 && x3 <= x1))) {
        ans = ((x2 - x1) - (r2 - r1)) * (y2 - y1);
    }
    // 4. 모서리가 깎이거나 중앙만 가려지는 경우 (최소 사각형은 원본 그대로)
    else {
        ans = (x2 - x1) * (y2 - y1);
    }
    cout << ans << endl;
    return 0;
}