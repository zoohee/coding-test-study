package BOJ;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class S9095_123더하기 {

	static int[] dp;
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int T = Integer.parseInt(br.readLine());
		for(int t=1; t<=T; t++) {
			int n = Integer.parseInt(br.readLine());
			
			dp = new int[Math.max(4, n+1)];
			dp[1] = 1;
			dp[2] = 2;
			dp[3] = 4;
			for(int i=4; i<=n; i++) {
				dp[i] = dp[i-3] + dp[i-2] + dp[i-1];
			}
			
			System.out.println(dp[n]);
		}
	}
}
