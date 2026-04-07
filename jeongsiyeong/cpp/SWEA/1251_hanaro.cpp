#include <iostream>
#include <vector>
#include <cmath>

#define ll long long
using namespace std;

struct Point {
    ll x, y;
};

ll getDist(Point a, Point b) {
    return (a.x - b.x) * (a.x - b.x) + (a.y - b.y) * (a.y - b.y);
}

void solve(int tc) {
    int N;
    cin >> N;
    
    vector<Point> points(N);
    for (int i = 0; i < N; i++) cin >> points[i].x;
    for (int i = 0; i < N; i++) cin >> points[i].y;
    
    double E;
    cin >> E;

    vector<ll> minDist(N, -1); 
    vector<bool> visited(N, false);  

    minDist[0] = 0;
    ll totalDist = 0;

    for (int i = 0; i < N; i++) {
        ll minD = -1;
        int u = -1;

        for (int j = 0; j < N; j++) {
            if (!visited[j] && minDist[j] != -1) {
                if (minD == -1 || minDist[j] < minD) {
                    minD = minDist[j];
                    u = j;
                }
            }
        }

        visited[u] = true;
        totalDist += minD;

        for (int v = 0; v < N; v++) {
            if (!visited[v]) {
                ll dist = getDist(points[u], points[v]);
                if (minDist[v] == -1 || dist < minDist[v]) {
                    minDist[v] = dist;
                }
            }
        }
    }

    ll ans = round(totalDist * E);
    cout << "#" << tc << " " << ans << "\n";
}

int main() {
    // 입출력 속도 향상
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int T;
    if (cin >> T) {
        for (int i = 1; i <= T; i++) {
            solve(i);
        }
    }
    
    return 0;
}