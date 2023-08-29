package BOJ;

import java.io.*;
import java.util.*;

public class S2178_미로탐색 {
	static int n, m, graph[][];
	static int[] dx = {-1, 1, 0, 0};
	static int[] dy = {0, 0, -1, 1};
	static String s[];
	static boolean visited[][];
	static Queue<int[]> queue = new LinkedList<>();

	public static void main(String[] args) throws Exception {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());

		graph = new int[n][m];
		for(int i=0; i<n; i++) {
			s = br.readLine().split("");
			for(int j=0; j<m; j++) {
				graph[i][j] = Integer.parseInt(s[j]);
			}
		}
		
		visited = new boolean[n][m];
		visited[0][0] = true;
		bfs(0, 0);
		System.out.println(graph[n-1][m-1]);
	}
	
	public static void bfs(int x, int y) {
		queue.add(new int[] {x,y});
		
		while(!queue.isEmpty()) {
			int now[] = queue.poll();
			int nowX = now[0];
			int nowY = now[1];
			
			for(int i=0; i<4; i++) {
				int nextX = nowX + dx[i];
				int nextY = nowY + dy[i];
				
                if (nextX < 0 || nextY < 0 || nextX >= n || nextY >= m)
        		    continue;
		        if (visited[nextX][nextY] || graph[nextX][nextY] == 0)
            		continue;
            
                queue.add(new int[] {nextX, nextY});
		        graph[nextX][nextY] = graph[nowX][nowY] + 1;
        		visited[nextX][nextY] = true;
			}
		}
	}
}