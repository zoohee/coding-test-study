package SWEA;

import java.io.*;

public class A039_SWEA3289_서로소집합 {
	static int[] arr;
	
	public static void main(String[] args) throws Exception {
		System.setIn(new FileInputStream("input039.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringBuilder sb = new StringBuilder();

		int T = Integer.parseInt(br.readLine());
		
		for(int t=1; t<=T; t++) {
			sb.append("#").append(t).append(" ");
			String[] s = br.readLine().split(" ");
			int n = Integer.parseInt(s[0]);
			int m = Integer.parseInt(s[1]);
			
			arr = new int[n+1]; // 초기 집합 배열
			for(int i=0; i<n+1; i++) {
				arr[i] = i;
			}
			
			for(int i=0; i<m; i++) {
				s = br.readLine().split(" ");
				int a = Integer.parseInt(s[1]);
				int b = Integer.parseInt(s[2]);
				
				// 0이면 합집합 연산
				if(s[0].equals("0")) {
					union(a, b);
				} else {
					sb.append(getResult(a, b));
				}
			}
			sb.append("\n");
		}
		
		bw.write(sb.toString());
		bw.flush();
		bw.close();
		br.close();
	}

	private static int find(int a) {
		if(a==arr[a]) return a;
		return arr[a] = find(arr[a]);
	}
	
	private static boolean union(int a, int b) {
		int aRoot = find(a);
		int bRoot = find(b);
		
		if(aRoot == bRoot) return false;
		arr[bRoot] = aRoot;
		return true;
	}
	
	public static String getResult(int a, int b) {
		if(find(a) == find(b)) return "1";
		else return "0";
	}
}

// 105,952kb / 518ms
