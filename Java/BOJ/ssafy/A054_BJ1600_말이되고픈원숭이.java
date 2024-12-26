package BOJ.ssafy;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;

public class A054_BJ1600_말이되고픈원숭이 {

	static int[] dx = { -2, -1, 1, 2, 2, 1, -1, -2 };
	static int[] dy = { 1, 2, 2, 1, -1, -2, -2, -1 };
	static int[] dxx = { -1, 0, 1, 0 };
	static int[] dyy = { 0, 1, 0, -1 };
	static int K, H, W;
	static int[][] map;
	static int[][][] visited;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		K = Integer.parseInt(br.readLine());

		String[] s = br.readLine().split(" ");
		W = Integer.parseInt(s[0]);
		H = Integer.parseInt(s[1]);

		map = new int[H][W];
		visited = new int[H][W][K + 1];
		for (int i = 0; i < H; i++) {
			s = br.readLine().split(" ");
			for (int j = 0; j < W; j++) {
				map[i][j] = Integer.parseInt(s[j]);
			}
		}

		bfs();
	}

	public static void bfs() {
		Queue<int[]> que = new ArrayDeque<>();
		que.offer(new int[] { 0, 0, 0 }); // x, y, 말모양이동횟수

		while (!que.isEmpty()) {
			int[] cur = que.poll();
			int x = cur[0];
			int y = cur[1];
			int c = cur[2];

			if (x == H - 1 && y == W - 1) {
				System.out.println(visited[x][y][c]);
				return;
			}

			if (c < K) {
				for (int d = 0; d < 8; d++) {
					int nx = x + dx[d];
					int ny = y + dy[d];

					if (nx < 0 || nx >= H || ny < 0 || ny >= W)
						continue;
					if (map[nx][ny] == 1)
						continue;
					if (visited[nx][ny][c+1] != 0)
						continue;
					que.offer(new int[] { nx, ny, c+1 });
					visited[nx][ny][c + 1] = visited[x][y][c] + 1;
				}
			}

			for (int d = 0; d < 4; d++) {
				int nx = x + dxx[d];
				int ny = y + dyy[d];

				if (nx < 0 || nx >= H || ny < 0 || ny >= W)
					continue;
				if (map[nx][ny] == 1)
					continue;
				if (visited[nx][ny][c] != 0)
					continue;
				que.offer(new int[] { nx, ny, c });
				visited[nx][ny][c] = visited[x][y][c] + 1;
			}

		}
		
		System.out.println(-1);
	}
}
