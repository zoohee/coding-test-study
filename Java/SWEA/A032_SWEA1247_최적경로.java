package SWEA;

import java.io.*;
import java.util.*;

public class A032_SWEA1247_최적경로 {

	static int N, x, y, minDistance=Integer.MAX_VALUE, numbers[];
	static ArrayList<int[]> map = new ArrayList<>();
	
	public static void main(String[] args) throws Exception {
		System.setIn(new FileInputStream("input032.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringBuilder sb = new StringBuilder();
		
		int T = Integer.parseInt(br.readLine());
		for (int t=1; t<=T; t++) {
			N = Integer.parseInt(br.readLine());
			String s = br.readLine();
			StringTokenizer st = new StringTokenizer(s);
			
			for(int i=0; i<N+2; i++) {
				x = Integer.parseInt(st.nextToken());
				y = Integer.parseInt(st.nextToken());
				map.add(new int[] {x, y});
			}
			
			numbers = new int[N];
			permutation(0, 0);
			
			sb.append("#").append(t).append(" ").append(minDistance).append("\n");
			minDistance=Integer.MAX_VALUE;
			map.clear();
		}
		
		bw.write(sb.toString());
		bw.flush();
		bw.close();
		br.close();
	}
	
	
	private static void permutation(int cnt, int flag) { // cnt 자리에 들어갈 수를 뽑기
		if(cnt == N) {
			dist(numbers);
			return;
		}
		
		for (int i = 0; i < N; i++) {
			// 중복 체크
			if ((flag & 1 << i) != 0) continue;
			// 수 선택
			numbers[cnt] = i+2;
			// 다음 자리수 뽑기
			permutation(cnt + 1, flag | 1 << i);
		}
	}
	
	private static void dist(int[] order) {
		int tmp = 0;
		// 회사부터 첫 고객까지의 거리
		tmp += Math.abs(map.get(0)[0]-map.get(order[0])[0]) + 
				Math.abs(map.get(0)[1]-map.get(order[0])[1]);
		
		// 고객 사이의 거리
		for(int i=1; i<N; i++) {
			tmp += Math.abs(map.get(order[i-1])[0]-map.get(order[i])[0]) + 
					Math.abs(map.get(order[i-1])[1]-map.get(order[i])[1]);
			if (tmp > minDistance) {
				return;
			}
		}
		
		// 마지막 고객부터 집까지의 거리
		tmp += Math.abs(map.get(order[N-1])[0]-map.get(1)[0]) + 
				Math.abs(map.get(order[N-1])[1]-map.get(1)[1]);

		if(tmp < minDistance) {
			minDistance = tmp;
		}
		
		return;
	}
}

// 23104kb / 1985ms 