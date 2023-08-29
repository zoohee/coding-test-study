package BOJ;

import java.io.*;

public class S14501_퇴사 {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int n = Integer.parseInt(br.readLine());
		int[][] arr = new int[n][2];
		for(int i=0; i<n; i++) {
			String[] s = br.readLine().split(" ");
			for(int j=0; j<2; j++) {
				arr[i][j] = Integer.parseInt(s[j]);
			}
		}
		
		int[] dp = new int[n+1];
		for(int i=n-1; i>=0; i--) {
			if(i+arr[i][0] > n) {
				dp[i] = dp[i+1];
			} else {
				dp[i] = Math.max(dp[i+1], arr[i][1] + dp[i+arr[i][0]]);
			}
		}
		
		System.out.println(dp[0]);
	}

}
