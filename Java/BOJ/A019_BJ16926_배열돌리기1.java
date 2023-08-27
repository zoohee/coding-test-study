package BOJ;

import java.io.*;

public class A019_BJ16926_배열돌리기1 {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		String[] s = br.readLine().split(" ");
		int n = Integer.parseInt(s[0]);
		int m = Integer.parseInt(s[1]);
		int r = Integer.parseInt(s[2]);
		int tmp = 0;

		int[][] arr = new int[n][m];
		for (int i = 0; i < n; i++) {
			s = br.readLine().split(" ");
			for (int j = 0; j < m; j++) {
				arr[i][j] = Integer.parseInt(s[j]);
			}
		}

		for (int a = 0; a < r; a++) {
			for (int t = 0; t < Math.min(n, m) / 2; t++) {
				for (int i = 0; i < 4; i++) {
					if (i == 0) {
						tmp = arr[t][t];
						for (int j = t; j < m - t - 1; j++) {
							arr[t][j] = arr[t][j + 1];
						}
					} else if (i == 1) {
						for (int j = t; j < n - t - 1; j++) {
							arr[j][m - t - 1] = arr[j + 1][m - t - 1];
						}
					} else if (i == 2) {
						for (int j = m - t - 1; j > t; j--) {
							arr[n - t - 1][j] = arr[n - t - 1][j - 1];
						}
					} else {
						for (int j = n - t - 1; j > t + 1; j--) {
							arr[j][t] = arr[j - 1][t];
						}
						arr[t + 1][t] = tmp;
					}
				}
			}
		}
		
		for(int i=0; i<n; i++) {
			for(int j=0; j<m; j++) {
				sb.append(arr[i][j]+" ");
			}
			sb.append("\n");
		}
		
		System.out.println(sb);
	}

}

// 39312KB / 744ms
