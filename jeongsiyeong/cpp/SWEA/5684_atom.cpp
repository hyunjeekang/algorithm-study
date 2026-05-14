#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
int dx[4] = { 0, 0, -1, 1 };
int dy[4] = { 1, -1, 0, 0 };
const int INF = 987654321; 

struct Atom {
    int x, y, d, k;
};

struct Event {
    int time, u, v; 
    
    bool operator<(const Event& other) const {
        return time < other.time;
    }
};

int get_collision_time(Atom A, Atom B) {
    int rdx = dx[A.d] - dx[B.d];
    int rdy = dy[A.d] - dy[B.d];

    int tx = -1, ty = -1;

    if (rdx != 0) {
        if ((B.x - A.x) % rdx != 0) return INF; 
        tx = (B.x - A.x) / rdx;
        if (tx < 0) return INF; 
    } else {
        if (A.x != B.x) return INF; 
    }

    if (rdy != 0) {
        if ((B.y - A.y) % rdy != 0) return INF;
        ty = (B.y - A.y) / rdy;
        if (ty < 0) return INF;
    } else {
        if (A.y != B.y) return INF;
    }

    if (rdx != 0 && rdy != 0) {
        if (tx != ty) return INF;
        return tx;
    }

    if (rdx != 0) return tx;
    if (rdy != 0) return ty;

    return INF;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int T;
    cin >> T;

    for (int test_case = 1; test_case <= T; ++test_case) {
        int N;
        cin >> N;

        vector<Atom> atoms(N);
        for (int i = 0; i < N; ++i) {
            int x, y, d, k;
            cin >> x >> y >> d >> k;
            atoms[i] = { x * 2, y * 2, d, k }; 
        }

        vector<Event> events;

        for (int i = 0; i < N; ++i) {
            for (int j = i + 1; j < N; ++j) {
                int t = get_collision_time(atoms[i], atoms[j]);
                if (t != INF) {
                    events.push_back({ t, i, j });
                }
            }
        }

        sort(events.begin(), events.end());

        vector<int> dead_time(N, INF);
        int total = 0;

        for (const auto& ev : events) {
            int t = ev.time;
            int u = ev.u;
            int v = ev.v;

            if (dead_time[u] < t || dead_time[v] < t) continue;

            if (dead_time[u] == INF && dead_time[v] == INF) {
                dead_time[u] = t;
                dead_time[v] = t;
                total += atoms[u].k + atoms[v].k;
            }
            else if (dead_time[u] == t && dead_time[v] == INF) {
                dead_time[v] = t;
                total += atoms[v].k;
            }
            else if (dead_time[v] == t && dead_time[u] == INF) {
                dead_time[u] = t;
                total += atoms[u].k;
            }
        }

        cout << "#" << test_case << " " << total << "\n";
    }

    return 0;
}