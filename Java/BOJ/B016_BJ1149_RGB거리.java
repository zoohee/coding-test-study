package BOJ;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class B016_BJ1149_RGB거리 {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int n = Integer.parseInt(br.readLine());
		int[][] house = new int[n][3];
		
		for(int i=0; i<n; i++) {
			String[] s = br.readLine().split(" ");
			for(int j=0; j<3; j++) {
				house[i][j] = Integer.parseInt(s[j]);
			}
		}
		
		for(int i=1; i<n; i++) {
			for(int j=0; j<3; j++) {
				if(j==0) {
					house[i][j] += Math.min(house[i-1][1], house[i-1][2]);
				} else if(j==1) {
					house[i][j] += Math.min(house[i-1][0], house[i-1][2]);
				} else {
					house[i][j] += Math.min(house[i-1][0], house[i-1][1]);
				}
			}
		} 
		
		int minValue = house[n-1][0];
		for(int i=1; i<3; i++) {
			if(minValue > house[n-1][i]) {
				minValue = house[n-1][i];
			}
		}
		
		System.out.println(minValue);
	}

}
