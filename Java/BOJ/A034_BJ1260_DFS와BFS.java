package BOJ;

import java.io.*;
import java.util.*;

public class A034_BJ1260_DFS와BFS {

	static int[][] arr;
	static boolean[] visited;
	static StringBuilder sb = new StringBuilder();
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		String[] s = br.readLine().split(" ");
		int n = Integer.parseInt(s[0]);
		int m = Integer.parseInt(s[1]);
		int v = Integer.parseInt(s[2]);
		arr = new int[n+1][n+1];
		for(int i=0; i<m; i++) {
			s = br.readLine().split(" ");
			int from = Integer.parseInt(s[0]);
			int to = Integer.parseInt(s[1]);
			arr[from][to] = arr[to][from] = 1;
		}
		
		visited = new boolean[n+1];
		dfs(v);
		sb.append("\n");
		visited = new boolean[n+1];
		bfs(v);
		
		bw.write(sb.toString());
		bw.flush();
		bw.close();
		br.close();
	}
	
	public static void dfs(int start) {
		visited[start] = true;
		sb.append(start).append(" ");
		
		for (int i=1; i<arr[start].length; i++) {
			if(arr[start][i] == 1 && !visited[i]) {
				dfs(i);
			}
		}
	}
	
	
	public static void bfs(int start) {
		Queue<Integer> que = new ArrayDeque<>();
		que.offer(start);
		visited[start] = true;
		
		while(!que.isEmpty()) {
			int cur = que.poll();
			visited[cur] = true;
			sb.append(cur).append(" ");
			for(int i=0; i<arr[0].length; i++) {
				if(arr[cur][i] != 0 && !visited[i]) {
					que.offer(i);
					visited[i] = true;
				}
			}
		}
		
	}
	

}
