package BOJ;

import java.io.*;
import java.util.*;

public class A030_BJ6987_월드컵 {
	static int cnt, game[][];
	static List<int[]> pair = new ArrayList<>(), wdl;
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		game = new int[6][3];
		wdl = new ArrayList<int[]>(Arrays.asList(new int[] {0, 2}, 
												 new int[] {1, 1}, 
												 new int[] {2, 0}));
		// 입력 받기
		for(int t=0; t<4; t++) {
			int index = 0;
			String[] s = br.readLine().split(" ");
			for(int i=0; i<6; i++) {
				for (int j=0; j<3; j++) {
					game[i][j] = Integer.parseInt(s[index]);
					index++;
					
				}
			}
			
			// 가능한 대결 조합 저장
			for(int i=0; i<6; i++) {
				for(int j=i+1; j<6; j++) {
					pair.add(new int[] {i, j});
				}
			}
			
			cnt = 0;
			worldcup(0);
			sb.append(cnt).append(" ");
			
		}		
		
		System.out.println(sb);
	}
	
	public static void worldcup(int depth) {
		if (depth == 15) { // 대결 조합을 모두 해봤을 때
			cnt = 1;
			int sum = 0;
			for(int i=0; i<6; i++) {
				for (int j=0; j<3; j++) {
					sum += game[i][j];
				}
				if (sum != 0) { // 승 무 패가 모두 0이 아니면
					cnt = 0;
					break;
				}
			}
			return;
		}
		
		// 대결팀 1과 대결팀 2
		int g1 = pair.get(depth)[0];
		int g2 = pair.get(depth)[1];
		
		for (int i=0; i<3; i++) { // 승무패 돌려보는 반복문
			int x = wdl.get(i)[0]; 
			int y = wdl.get(i)[1];
			if(game[g1][x] > 0 && game[g2][y] > 0) { // 승무패의 횟수가 남아있으면
				game[g1][x] -= 1;
				game[g2][y] -= 1;
				worldcup(depth+1);
				game[g1][x] += 1;
				game[g2][y] += 1;
			}
		}

	}
}

// 11580KB / 84ms