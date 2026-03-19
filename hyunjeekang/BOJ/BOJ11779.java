import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class BOJ11779 {

	static StringBuilder sb = new StringBuilder();

	public static class Node implements Comparable<Node> {
		public int vertex, weight;

		public Node(int next, int weight) {
			this.vertex = next;
			this.weight = weight;
		}

		@Override
		public int compareTo(Node o) {
			return Integer.compare(this.weight, o.weight);
		}
	}

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;

		int n = Integer.parseInt(br.readLine());
		int m = Integer.parseInt(br.readLine());

		ArrayList<int[]>[] graph = new ArrayList[n + 1];
		for (int i = 1; i < n + 1; i++) {
			graph[i] = new ArrayList<>();
		}

		for (int i = 0; i < m; i++) {
			st = new StringTokenizer(br.readLine());
			graph[Integer.parseInt(st.nextToken())]
					.add(new int[] { Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()) });
		}

		st = new StringTokenizer(br.readLine());
		dijkstra(n, graph, Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
		System.out.println(sb);
	}

	public static void dijkstra(int n, ArrayList<int[]>[] graph, int start, int end) {

		int[] dist = new int[n + 1];
		int[] minPrev = new int[n + 1];
		for (int i = 0; i < n + 1; i++) {
			dist[i] = Integer.MAX_VALUE;
		}
		PriorityQueue<Node> pq = new PriorityQueue<>();

		dist[start] = 0;
		minPrev[start] = -1;
		pq.add(new Node(start, 0));

		while (!pq.isEmpty()) {
			Node curNode = pq.poll();
			
			if(dist[curNode.vertex] < curNode.weight) continue;

			for (int[] nextNode : graph[curNode.vertex]) {

				if (dist[nextNode[0]] == Integer.MAX_VALUE || dist[nextNode[0]] > dist[curNode.vertex] + nextNode[1]) {

					dist[nextNode[0]] = dist[curNode.vertex] + nextNode[1];
					minPrev[nextNode[0]] = curNode.vertex;
					pq.add(new Node(nextNode[0], nextNode[1]));
				}

			}
		}

		sb.append(dist[end]).append("\n");
		
		ArrayList<Integer> path = new ArrayList<>();
		path.add(end);
		
		int prevNode = minPrev[end];
		while(prevNode != -1) {
			path.add(prevNode);
			prevNode = minPrev[prevNode];
		}
		
		sb.append(path.size()).append("\n");
		Collections.reverse(path);
		
		for (Integer integer : path) {
			sb.append(integer).append(" ");
		}

	}

}
