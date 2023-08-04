package SWEA;

import java.io.*;

public class B003_SWEA2001_파리퇴치 {
	static int n, m, arr[][], maxValue, tmp;
	static String str[];
	public static void main(String[] args) throws Exception {
		System.setIn(new FileInputStream("input003.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		
		for (int t=0; t<T; t++) {
			str = br.readLine().split(" ");
			n = Integer.parseInt(str[0]);
			m = Integer.parseInt(str[1]);
			
			arr = new int[n][n];
			for(int i=0; i<n; i++) {
				str = br.readLine().split(" ");
				for(int j=0; j<n; j++) {
					arr[i][j] = Integer.parseInt(str[j]);
				}
			}
			
			for(int i=0; i<n-m+1; i++) {
				for(int j=0; j<n-m+1; j++) {
					for(int k=i; k<i+m; k++) {
						for(int l=j; l<j+m; l++) {
							tmp += arr[k][l];
						}
					}
					if (tmp > maxValue) {
						maxValue = tmp;
					}
					tmp = 0;
				}
			}
			
			System.out.println("#"+(t+1)+" "+maxValue);
			maxValue = 0;
		}
		
	}

}

// 18880kb / 109ms
