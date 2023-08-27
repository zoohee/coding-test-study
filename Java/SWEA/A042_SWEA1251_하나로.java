package SWEA;

import java.awt.*;
import java.io.*;
import java.util.*;

public class A042_SWEA1251_하나로 {
	
	static class Edge implements Comparable<Edge> {
		int from, to; 
		double weight;
		
		public Edge(int from, int to, double weight) {
			super();
			this.from = from;
			this.to = to;
			this.weight = weight;
		}
		
		@Override
		public int compareTo(Edge o) {
			return Double.compare(this.weight, o.weight);
		}
	}

	public static int N, parents[];
    public static double E;
    public static Point[] land;
    public static ArrayList<Edge> edgeList;
    
	public static void main(String[] args) throws Exception {
		System.setIn(new FileInputStream("input042.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringBuilder sb = new StringBuilder();

		int T = Integer.parseInt(br.readLine());
		
		for(int t=1; t<=T; t++) {
			N = Integer.parseInt(br.readLine());
			land = new Point[N];
            parents = new int[N];
            
			String[] xList = br.readLine().split(" ");
			String[] yList = br.readLine().split(" ");
			for(int i=0; i<N; i++) {
				land[i] = new Point(0, 0);
				land[i].x = Integer.parseInt(xList[i]);
				land[i].y = Integer.parseInt(yList[i]);
			}
			double E = Double.parseDouble(br.readLine());
			
            // 모든 간선의 비용을 저장
            edgeList = new ArrayList<>();
            for (int i = 0; i < N; i++) {
                for (int j = i + 1; j < N; j++) {
                    double distX = Math.abs(land[i].x - land[j].x);
                    double distY = Math.abs(land[i].y - land[j].y); 
                    edgeList.add(new Edge(i, j, distX * distX + distY * distY));
                }
            }
            edgeList.sort(null);
            
            make();
            
            int cnt = 0;
            Double res = 0.0;
            for (Edge edge : edgeList) {
                if(union(edge.from, edge.to)) {
                    res += edge.weight;
                    if(++cnt == N - 1) break;
                }
            }
            
            sb.append("#").append(t).append(" ").append(Math.round(res*E)).append("\n");
		}
		
		bw.write(sb.toString());
		bw.flush();
		bw.close();
		br.close();
	}
	
	private static boolean union(int a, int b) {
        int aRoot = find(a);
        int bRoot = find(b);
        // 사이클이 형성되면
        if(aRoot == bRoot) return false;
        parents[bRoot] = aRoot;
        return true;
    }
 
    private static int find(int a) {
        if(a == parents[a]) return a;
        return parents[a] = find(parents[a]);
    }
 
    private static void make() {
        for (int i = 0; i < N; i++) {
            parents[i] = i;
        }
    }    
}
