package BOJ.ssafy;

import java.io.*;
import java.util.*;

public class A040_BJ15683_감시 {
	static int[][] arr;
	static int[][][] dir = new int[][][] {{{0},{1},{2},{3}}, {{0,2},{1,3}}, {{0,1},{1,2},{2,3},{3,0}}, 
											{{0,1,3},{0,1,2},{1,2,3},{2,3,0}}, {{0,1,2,3}}};
											// 0: 북, 1: 동, 2: 남, 3:서
	static int n, m, answer=Integer.MAX_VALUE;
	static int[] dx = new int[] {-1, 0, 1, 0}; // 북 동 남 서
	static int[] dy = new int[] {0, 1, 0, -1};
	static ArrayList<int[]> cctv; // cctv 인덱스, 번호 저장할 어레이
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		String[] s = br.readLine().split(" ");
		n = Integer.parseInt(s[0]);
		m = Integer.parseInt(s[1]);
		
		arr = new int[n][m];
		cctv = new ArrayList<>();
		for(int i=0; i<n; i++) {
			s = br.readLine().split(" ");
			for(int j=0; j<m; j++) {
				arr[i][j] = Integer.parseInt(s[j]);
				if(arr[i][j] != 0 && arr[i][j] != 6) { // 1 2 3 4 5는 cctv에 저장
					cctv.add(new int[] {i, j, arr[i][j]});
				}
			}
		}
		
		dfs(arr, 0);
		System.out.println(answer);
	}
	
	public static void dfs(int[][] office, int cnt) { // dfs 탐색
		int[][] tmp = new int[n][m];
		tmp = deepCopy(office); // 임시적으로 바꿀 그래프 저장
		
		if(cnt == cctv.size()) { // cctv 배열 다 돌았으면 (3개면 3개)
			int c = 0;
			for(int i=0; i<n; i++) {
				for(int j=0; j<m; j++) {
					if(tmp[i][j] == 0) {
						c += 1; // 사각지대 칸 수 저장
					}
				}
			}
			answer = Math.min(answer, c);
			return;
		}
		
		int x = cctv.get(cnt)[0];
		int y = cctv.get(cnt)[1];
		int cam = cctv.get(cnt)[2];
		
		for (int[] i: dir[cam-1]) { // cctv 번호의 방향 배열 가져오기
			tmp = watch(x, y, i, tmp); // 방향대로 cctv가 감시할 수 있는 곳 체크
			dfs(tmp, cnt+1); // 감시한 곳 저장한 채로 다음 cctv가 감시할 수 있는 곳 체크
			tmp = deepCopy(office); // 원래대로 돌려놓기
		}
		
		
	}

	public static int[][] watch(int x, int y, int[] dir, int[][] tmp) {
		for (int d: dir) { // 방향
			int nx = x;
			int ny = y;
			
			while(true) { // 맵 경계나 벽을 만날 때까지 뻗어나가기
				nx += dx[d];
				ny += dy[d];
				if(nx >= 0 && nx < n && ny >= 0  && ny < m && tmp[nx][ny]!=6) { // 경계나 벽 만나면
					if (tmp[nx][ny] == 0) { // 감시 영역 체크
						tmp[nx][ny] = -1;
					} 
				} else {
					break;
				}
			}
		}
		return tmp;
	}
	
	private static int[][] deepCopy(int[][] original) { // 배열 복사 함수
		int[][] copy = new int[original.length][];
		for (int i = 0; i < original.length; i++) {
			copy[i] = Arrays.copyOf(original[i], original[i].length);
		}
		return copy;
	}
}

// 127264kb / 268ms
