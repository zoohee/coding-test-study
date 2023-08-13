package SWEA;

import java.io.*;

public class A024_SWEA4012_요리사 {

	static int ing[][], index[], minValue=Integer.MAX_VALUE, n;
	static boolean visited[];

	public static void main(String[] args) throws Exception {
		System.setIn(new FileInputStream("input024.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int T = Integer.parseInt(br.readLine());
		for (int t = 1; t <= T; t++) {
			n = Integer.parseInt(br.readLine());

			ing = new int[n][n];
			index = new int[n];
			visited = new boolean[n];
			
			for (int i = 0; i < n; i++) {
				index[i] = i;
				String[] s = br.readLine().split(" ");
				for (int j = 0; j < n; j++) {
					ing[i][j] = Integer.parseInt(s[j]);
				}
			}

			comb(0, n / 2);
			System.out.println("#"+t+" "+minValue);
			minValue = Integer.MAX_VALUE;
		}
	}

	public static void comb(int start, int r) {
		// n/2개 선택되면
		if (r == 0) {
			int a = 0;
			int b = 0;
			// 배열 대각선 모양 만큼만 돌리기
			for (int i = 0; i < n-1; i++) {
				for (int j=i+1; j< n; j++) {
					// 부분집합으로 선택된 원소면 값 저장
					if (visited[i] == true && visited[j]==true)	{
						a += ing[i][j] + ing[j][i];
					}
					// 부분집합으로 선택되지 않은 원소면 값 저장
					else if (visited[i] == false && visited[j]==false) {	
						b += ing[i][j] + ing[j][i];
					}
				}
			}
			
			// 최소가 되는 절대값 갱신
			if (minValue > Math.abs(a-b)) {
				minValue = Math.abs(a-b);
			}
			return;
		} else { // 재귀로 부분집합 구하기
			for (int i = start; i < n; i++) {
				visited[i] = true;
				comb(i + 1, r - 1);
				visited[i] = false;
			}
		}
	}
}

// 22708KB / 250ms
