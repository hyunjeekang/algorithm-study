import java.util.*;
import java.io.*;

public class BOJ2638 {

	static final int[] drs = { 0, 0, -1, 1 }, dcs = { -1, 1, 0, 0 };

	static int N, M, cnt;
	static int[][] grid;

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());

		grid = new int[N][M];
		for (int r = 0; r < N; r++) {
			st = new StringTokenizer(br.readLine());
			for (int c = 0; c < M; c++) {
				grid[r][c] = Integer.parseInt(st.nextToken());
				if (grid[r][c] == 1)
					cnt++;
			}
		}

		System.out.println(cheese(N, M, grid, cnt));

	}

	private static int cheese(int N, int M, int[][] grid, int cnt) {
		int time = 0;

		while (cnt > 0) {
			Queue<int[]> q = new LinkedList<>();
			int[][] visited = new int[N][M];
			List<int[]> meltList = new ArrayList<>();

			// 외부 공기 0,0에서 bfs 탐색 시작
			q.add(new int[] { 0, 0 });
			visited[0][0] = -1;

			while (!q.isEmpty()) {
				int[] c = q.poll();

				for (int i = 0; i < 4; i++) {
					int nr = c[0] + drs[i];
					int nc = c[1] + dcs[i];

					if (!inBounds(N, M, nr, nc))
						continue;

					// 외부 공기 탐색 
					if (grid[nr][nc] == 0 && visited[nr][nc] == 0) {
						visited[nr][nc] = -1;
						q.add(new int[] { nr, nc });
					}
					
					// 치즈 만난 경우 
					else if (grid[nr][nc] == 1) {
						visited[nr][nc]++;

						// 2면 공기 -> list에 추가
						if (visited[nr][nc] == 2) {
							meltList.add(new int[] { nr, nc });
						}
					}
				}
			}

			// 이번 턴에 녹을 치즈 처리
			for (int[] cur : meltList) {
				grid[cur[0]][cur[1]] = 0;
				cnt--;
			}

			time++;
		}

		return time;
	}

	private static boolean inBounds(int N, int M, int r, int c) {
		return 0 <= r && r < N && 0 <= c && c < M;
	}

}
