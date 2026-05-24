import java.io.*;
import java.util.*;

public class SWEA1953 {

	static int[][] dirs = { { -1, 0 }, { 1, 0 }, { 0, -1 }, { 0, 1 } }; // 상하좌우
	static final int[][] pipes = {
			{},
		    { 0, 1, 2, 3 },
		    { 0, 1 },
		    { 2, 3 },
		    { 0, 3 },
		    { 1, 3 },
		    { 1, 2 },
		    { 0, 2 }
		};
	static int T, N, M, R, C, L, result;
	static int[][] map;

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st;

		T = Integer.parseInt(br.readLine());
		for (int t = 1; t <= T; t++) {
			st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken());
			M = Integer.parseInt(st.nextToken());
			R = Integer.parseInt(st.nextToken());
			C = Integer.parseInt(st.nextToken());
			L = Integer.parseInt(st.nextToken());

			map = new int[N][M];
			for (int r = 0; r < N; r++) {
				st = new StringTokenizer(br.readLine());
				for (int c = 0; c < M; c++) {
					map[r][c] = Integer.parseInt(st.nextToken());
				}
			}

			result = solution(R, C, map);

			sb.append("#").append(t).append(" ").append(result).append("\n");
		}
		System.out.println(sb);

	}

	public static int solution(int R, int C, int[][] map) {
		
		int res = 1;
		boolean[][] visited = new boolean[N][M];
		Queue<int[]> q = new LinkedList<>();

		visited[R][C] = true;
		q.add(new int[] { R, C, 1 });

		while (!q.isEmpty()) {

			int[] cur = q.poll();
			int pipe = map[cur[0]][cur[1]];

			if (pipe != 0 && cur[2] < L) {
				for (int dir : pipes[pipe]) {
					int nr = cur[0] + dirs[dir][0];
					int nc = cur[1] + dirs[dir][1];
					if (inBounds(nr, nc) && !visited[nr][nc] && checkNextPipe(nr, nc, dir)) {
						res++;
						visited[nr][nc] = true;
						q.add(new int[] { nr, nc, cur[2] + 1 });
					}
				}
			}

		}

		return res;
	}
	
	public static boolean checkNextPipe(int r, int c, int curDir) {
		int nextPipe = map[r][c];
		int targetDir = curDir % 2 == 0 ? curDir + 1 : curDir - 1;
		
		if(nextPipe == 0) return false;
		
		for (int dir : pipes[nextPipe]) {
			if (dir == targetDir)
				return true;
		}

		return false;
	}

	public static boolean inBounds(int r, int c) {
		return 0 <= r && r < N && 0 <= c && c < M;
	}
}
