package BOJ.ssafy;

import java.io.*;
import java.util.*;

public class S1240_노드사이의거리 {
	private static ArrayList<int[]>[] nodes;
	private static boolean[] visited;
	private static int[] answer;
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] s = br.readLine().split(" ");
		int n = Integer.parseInt(s[0]);
		int m = Integer.parseInt(s[1]);
		
		nodes = new ArrayList[n+1];
		for (int i=0; i<=n; i++) {
			nodes[i] = new ArrayList<int[]>();
		}
		
		for(int i=0; i<n-1; i++) {
			s = br.readLine().split(" ");
			int a = Integer.parseInt(s[0]);
			int b = Integer.parseInt(s[1]);
			int dist = Integer.parseInt(s[2]);
			nodes[a].add(new int[] {b, dist});
			nodes[b].add(new int[] {a, dist});
		}
		
		for(int i=0; i<m; i++) {
			answer = new int[n+1];
			s = br.readLine().split(" ");
			int a = Integer.parseInt(s[0]);
			int b = Integer.parseInt(s[1]);
			visited = new boolean[n+1];
			bfs(a, b);
			System.out.println(answer[b]);
		}
	}
	
	public static void bfs(int a, int b) {
		Queue<Integer> que = new ArrayDeque();
		
		que.offer(a);
		
		while(!que.isEmpty()) {
			int current = que.poll();
			visited[current] = true;
			for (int i=0; i<nodes[current].size(); i++) {
				if(!visited[nodes[current].get(i)[0]]) {
					answer[nodes[current].get(i)[0]] += answer[current] + nodes[current].get(i)[1];
					que.offer(nodes[current].get(i)[0]);
				}
			}
			
		}
	}
}

//5 1
//1 2 1
//2 3 1
//3 4 10
//3 5 1
//1 5
