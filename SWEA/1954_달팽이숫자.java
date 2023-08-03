import java.util.*;

public class B002_SWEA1954_달팽이숫자 {

	public static int arr[][], x, y, d;
	public static boolean visited[][];
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int test = sc.nextInt();
		
		for (int t=0; t<test; t++) {
			int n = sc.nextInt();
			arr = new int[n][n];
			visited = new boolean[n][n];
			
			snail(n);
			System.out.println("#"+(t+1));
			for(int i=0;i<n;i++) {
				for (int j=0;j<n;j++) {
					System.out.print(arr[i][j]+" ");
				}
				System.out.println();
			}
			
			// 초기화
			x = 0;
			y = 0;
			d = 0;
		}
	}
	
	public static void snail(int n) {
		//우하좌상
		int[] dx = {0, 1, 0, -1};
		int[] dy = {1, 0, -1, 0};
		
		for (int i=1; i<=n*n; i++) {
			arr[x][y] = i;
			// 배열을 벗어나거나 이미 숫자가 있으면 방향 전환
			if (x + dx[d] >= n || x + dx[d] < 0 || y+dy[d] >=n || y+dy[d] < 0 || 
					arr[x+dx[d]][y+dy[d]]!=0) {
				d = (d+1) % 4;
			}
			
			// 움직이기
			x += dx[d];
			y += dy[d];
		}
	}
}

// 21036kb / 144ms