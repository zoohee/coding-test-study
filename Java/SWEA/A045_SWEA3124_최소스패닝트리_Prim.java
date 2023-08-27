package SWEA;

import java.io.*;
import java.util.*;

public class A045_SWEA3124_최소스패닝트리_Prim {
	
	static class Vertex implements Comparable<Vertex>{
		int no, weight; // 정점 번호, 트리 정점과 연결했을 때의 간선비용
		public Vertex(int no, int weight) {
			this.no = no;
			this.weight = weight;
		}
		
		@Override
		public int compareTo(Vertex o) {
			return Integer.compare(this.weight, o.weight);
		}
	}

	static int V, E;
	static ArrayList<Vertex>[] adjList;
	
	public static void main(String[] args) throws Exception {
		System.setIn(new FileInputStream("input045.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringBuilder sb = new StringBuilder();

		int T = Integer.parseInt(br.readLine());
		for(int t=1; t<=T; t++) {
			String[] s = br.readLine().split(" ");
			V = Integer.parseInt(s[0]);
			E = Integer.parseInt(s[1]);
			
			adjList = new ArrayList[V+1];
			for(int i=0; i<=V; i++) {
				adjList[i] = new ArrayList<>();
			}
			
			for(int i=0; i<E; i++) {
				s = br.readLine().split(" ");
				int x = Integer.parseInt(s[0]);
				int y = Integer.parseInt(s[1]);
				int w = Integer.parseInt(s[2]);
				adjList[x].add(new Vertex(y, w));
				adjList[y].add(new Vertex(x, w));
			}
			
			boolean[] visited = new boolean[V+1];
			PriorityQueue<Vertex> pQueue = new PriorityQueue<>();
			
			pQueue.offer(new Vertex(1, 0));
			
			long result = 0; // 최소 신장트리 비용
			int min = 0, minVertex = 0, cnt = 0;
			
			while(!pQueue.isEmpty()) {
				// step1 : 미방문(비트리) 정점 중 최소간선비용의 정점을 선택
				Vertex cur = pQueue.poll();
				minVertex = cur.no;
				min = cur.weight;
				if(visited[minVertex]) continue;
				
				// step 2 : 방문(트리) 정점에 추가
				visited[minVertex] = true; // 방문 처리
				result += min; // 신장트리 비용 누적
				if(++cnt==V) break;
				
				for(int i=0;i<adjList[minVertex].size();i++) {
					Vertex next = adjList[minVertex].get(i);
					if(visited[next.no] == true) continue;
					pQueue.add(next);
				}
				
			}
			
			sb.append("#").append(t).append(" ").append(result).append("\n");
		}
		
		bw.write(sb.toString());
		bw.flush();
		bw.close();
		br.close();
	}

}


// 220420kb / 3313ms
