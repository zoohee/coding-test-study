package SWEA;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;

public class A023_SWEA5215_햄버거다이어트 {
	
	static int info[][], n, l, maxScore;
	static boolean[] isSelected;
	
	public static void main(String[] args) throws Exception {
		System.setIn(new FileInputStream("input023.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int T = Integer.parseInt(br.readLine());
		
		for(int t=1; t<=T; t++) {
			String[] s = br.readLine().split(" ");
			n = Integer.parseInt(s[0]);
			l = Integer.parseInt(s[1]);
			
			info = new int[n][2];
			isSelected = new boolean[n];
			for (int i=0; i<n; i++) {
				s = br.readLine().split(" ");
				info[i][0] = Integer.parseInt(s[0]);
				info[i][1] = Integer.parseInt(s[1]);
			}
			
			generateSubset(0);
			System.out.println("#"+t+" "+maxScore);
			maxScore = 0;
		}
	}
	
	private static void generateSubset(int cnt) {
		
		// 부분집합 선택 끝나면
		if (cnt == n) {
			int tmpScore = 0;
			int sumCalories = 0;
			for (int i = 0; i < n; i++) {
				if(isSelected[i]) { // 부분집합 원소면 점수, 칼로리 계산
					sumCalories += info[i][1];
					tmpScore += info[i][0];
				}
				
				if(sumCalories > l) { // 제한 칼로리보다 높으면 더 비교할 필요 없음
					tmpScore = 0;
					break;
				}
			}
			
			if(maxScore < tmpScore) { // 칼로리 제한 안넘었으면 최대 점수와 비교 후 교체
				maxScore = tmpScore;
			}
			
			return;
		}
		
		isSelected[cnt] = true;
		generateSubset(cnt+1);
		isSelected[cnt] = false;
		generateSubset(cnt+1);
	}

}

// 21786kb / 745ms