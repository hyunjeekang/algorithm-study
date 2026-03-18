import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Collections;
import java.util.HashMap;
import java.util.Map;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class BOJ7662 {

	static int T, k, value;
	static String command;
	static PriorityQueue<Integer> minPQ, maxPQ;
	static Map<Integer, Integer> map;

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st;

		T = Integer.parseInt(br.readLine().strip());

		for (int t = 0; t < T; t++) {
			k = Integer.parseInt(br.readLine().strip());

			minPQ = new PriorityQueue<>();
			maxPQ = new PriorityQueue<>(Collections.reverseOrder());
			map = new HashMap<>();

			for (int kk = 0; kk < k; kk++) {
				st = new StringTokenizer(br.readLine());
				command = st.nextToken();
				value = Integer.parseInt(st.nextToken());

				if (command.equals("I")) {
					minPQ.add(value);
					maxPQ.add(value);
					map.put(value, map.getOrDefault(value, 0) + 1);

				} else { // command == "D"
					PriorityQueue<Integer> targetPQ = (value == 1) ? maxPQ : minPQ;
					remove(targetPQ, map);

					if (!targetPQ.isEmpty()) {
						int removed = targetPQ.poll();
						if (map.get(removed) == 1)
							map.remove(removed);
						else
							map.put(removed, map.get(removed) - 1);
					}

				}
			}

			remove(maxPQ, map);
			remove(minPQ, map);

			if (maxPQ.isEmpty())
				sb.append("EMPTY\n");
			else
				sb.append(maxPQ.peek()).append(" ").append(minPQ.peek()).append("\n");
		}

		System.out.println(sb);

	}

    // 의도한 값이 나올 때까지 삭제
	static void remove(PriorityQueue<Integer> pq, Map<Integer, Integer> map) {
		while (!pq.isEmpty() && !map.containsKey(pq.peek())) {
			pq.poll();
		}
	}

}