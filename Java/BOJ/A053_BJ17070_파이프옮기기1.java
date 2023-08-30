package BOJ;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class A053_BJ17070_파이프옮기기1 {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int N = Integer.parseInt(br.readLine());
		
		int[][] map = new int[N][N];
		int[][][] dp = new int[N][N][3];
		for(int i=0; i<N; i++) {
			String[] s = br.readLine().split(" ");
			for(int j=0; j<N; j++) {
				map[i][j] = Integer.parseInt(s[j]);
			}
		}
		
		for(int i=0; i<N; i++) {
			for(int j=1; j<N; j++) {
				
				if(map[i][j] == 1) continue; // 벽 넘어감
				dp[i][j][0] = dp[i][j-1][0] + dp[i][j-1][1]; // 가로 (가로와 대각선 받기)
				
				if(i==0 && j==1) dp[0][1][0] = 1;
				
				if(i==0) continue; // 0행 볼 필요 없음
				dp[i][j][2] = dp[i-1][j][1] + dp[i-1][j][2]; // 세로 (대각선과 세로 받기)
				
				if(map[i-1][j] == 1 || map[i][j-1] == 1) continue; // 대각선이 차지하는 3칸 중 벽이 있으면 넘어감
				dp[i][j][1] = dp[i-1][j-1][0] + dp[i-1][j-1][1] + dp[i-1][j-1][2];
				
			}
		}
		
		int answer = 0;
		for(int i=0; i<3; i++) {
			answer += dp[N-1][N-1][i];
		}
		System.out.println(answer);
	}

}

// 11580KB / 80ms