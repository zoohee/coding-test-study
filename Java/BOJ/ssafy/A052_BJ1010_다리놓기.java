package BOJ.ssafy;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class A052_BJ1010_다리놓기 {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		for(int t=0; t<N; t++) {
			String[] s = br.readLine().split(" ");
			int n = Integer.parseInt(s[0]);
			int m = Integer.parseInt(s[1]);
			int[][] dp = new int[m+1][n+1];
			
			for(int i=0; i <= m; i++) {
				for(int j=0, end = Math.min(i, n); j<=end; j++) {
					if(j==0 || i==j) dp[i][j] = 1;
					else dp[i][j] = dp[i-1][j-1] + dp[i-1][j];
				}
			}
			
			System.out.println(dp[m][n]);
		}
		
		
	}

}
