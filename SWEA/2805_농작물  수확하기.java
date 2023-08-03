import java.io.*;

public class A006_SWEA2805_농작물수확하기 {
	private static int answer;
	
	public static void main(String[] args) throws Exception {
		System.setIn(new FileInputStream("input006.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int test = Integer.parseInt(br.readLine());
		
		for (int t = 0; t < test; t++) {
			int n = Integer.parseInt(br.readLine());
			int[][] goods = new int[n][n];
			int mid = n/2;
			for (int i = 0; i < n; i++) {
				String[] Line = br.readLine().split("");
				for (int j = 0; j < n; j++) {
					goods[i][j] = Integer.parseInt(Line[j]);
					if (i>=0 && i<=mid && j >= mid-i && j<=mid+i) { // 위쪽 다이아몬드
						answer += goods[i][j];
					} else if (i>mid && i<n && j >= mid-(n-i-1) && j <=mid+(n-i-1)) { // 아래쪽 다이아몬드
						answer += goods[i][j];
					}

				}
			}
			
			System.out.println("#"+(t+1)+" "+answer);
			answer = 0;
		}
	}

}
