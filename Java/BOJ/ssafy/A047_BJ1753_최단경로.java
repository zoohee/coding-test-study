package BOJ.ssafy;

import java.io.*;
import java.util.*;

public class A047_BJ1753_최단경로 {

	static class Node implements Comparable<Node> {
		int end, weight;

		public Node(int end, int weight) {
			this.end = end;
			this.weight = weight;
		}

		@Override
		public int compareTo(Node o) {
			return weight - o.weight;
		}
	}

	static List<Node>[] adjList;
	static int V, E, K, dest;
	static int[] parents, dist;
	static boolean[] visited;
	static final int INF = Integer.MAX_VALUE;
	static StringBuilder sb = new StringBuilder();

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		String[] s = br.readLine().split(" ");
		V = Integer.parseInt(s[0]);
		E = Integer.parseInt(s[1]);
		K = Integer.parseInt(br.readLine());

		adjList = new ArrayList[V+1];
		for (int i = 1; i <= V; i++) {
			adjList[i] = new ArrayList<>();
		}

		for (int i = 0; i < E; i++) {
			s = br.readLine().split(" ");
			int from = Integer.parseInt(s[0]);
			int to = Integer.parseInt(s[1]);
			int weight = Integer.parseInt(s[2]);
			adjList[from].add(new Node(to, weight));
		}

		dist = new int[V+1];
		Arrays.fill(dist, INF);
		dijkstra(K);
		for(int i = 1; i <= V; i++){
            if(dist[i] == INF) sb.append("INF\n");
            else sb.append(dist[i] + "\n");
        }

		System.out.println(sb);
	}

	private static void dijkstra(int start) {
		PriorityQueue<Node> queue = new PriorityQueue<>(); // 최소힙 형태로 사용 (가중치에 따라)
		boolean[] check = new boolean[V + 1]; // 최단 경로로 확정 처리
		queue.add(new Node(start, 0)); // 시작 노드 큐에 추가
		dist[start] = 0; // 시작 정점 0으로 설정

		while (!queue.isEmpty()) {
			Node curNode = queue.poll();
			int cur = curNode.end;

			if (check[cur] == true) // 이미 최단 경로로 확정되었으면 건너뜀
				continue;
			check[cur] = true; // 

			for (Node node : adjList[cur]) { 
				if (dist[node.end] > dist[cur] + node.weight) { // 현재까지의 최단거리가 현재 정점~해당 노드까지 가중치 누적보다 크면
					dist[node.end] = dist[cur] + node.weight;
					queue.add(new Node(node.end, dist[node.end]));
				}
			}
		}
	}
}

// 15250KB / 924ms
