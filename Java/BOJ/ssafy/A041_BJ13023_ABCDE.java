package BOJ.ssafy;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class A041_BJ13023_ABCDE {
	
	static ArrayList<Integer>[] list;
	static boolean[] visited;
	static int n, m;
	static boolean isPossible;
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] s = br.readLine().split(" ");
		
		n = Integer.parseInt(s[0]);
		m = Integer.parseInt(s[1]);
		
		list = new ArrayList[n];
		for(int i=0; i<n; i++) {
			list[i] = new ArrayList<>();
		}
		visited = new boolean[n];
		for(int i=0; i<m; i++) {
			s = br.readLine().split(" ");
			int a = Integer.parseInt(s[0]);
			int b = Integer.parseInt(s[1]);
			
			list[a].add(b);
			list[b].add(a);
		}
		
		for(int i=0; i<n; i++) {
			visited = new boolean[n];
			dfs(i, 0);
			if(isPossible) break;
		}
		
		if(isPossible) System.out.println(1);
		else System.out.println(0);
		
	}

	public static void dfs(int start, int cnt) {
		if(cnt==4) {
			isPossible = true;
			return;
		}
		
		visited[start] = true;
		
		for(int i=0; i<list[start].size(); i++) {
			if(!list[list[start].get(i)].isEmpty() && !visited[list[start].get(i)]) {
				visited[list[start].get(i)] = true;
				dfs(list[start].get(i), cnt+1);
				visited[list[start].get(i)] = false;
			}
		}
	}
}

// 18624ms / 280ms
