package BOJ;

import java.io.*;
import java.util.*;

public class A031_BJ3109_빵집 {

	static int r, c, ans, dir[] = { -1, 0, 1 };
	static String[][] bakery;
	static boolean[][] visited;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		String[] s = br.readLine().split(" ");
		r = Integer.parseInt(s[0]);
		c = Integer.parseInt(s[1]);

		bakery = new String[r][c];
		for (int i = 0; i < r; i++) {
			s = br.readLine().split("");
			for (int j = 0; j < c; j++) {
				bakery[i][j] = s[j];
			}
		}

		for (int i = 0; i < r; i++) {
			pipeline(i, 0);
		}

		System.out.println(Arrays.deepToString(bakery));
		System.out.println(ans);
	}

	private static boolean pipeline(int x, int y) {

		if (y == c - 1) { // 끝까지 오면 카운트
			ans++;
			return true;
		}

		for (int d = 0; d < 3; d++) {
			int nx = x + dir[d];
			int ny = y + 1;

			// 범위 밖
			if (nx < 0 || ny < 0 || nx == r || ny == c)
				continue;

			// 못지나는 곳
			if (bakery[nx][ny].equals("x") || bakery[nx][ny].equals("-"))
				continue;

			// 방문했음을 표시
			bakery[nx][ny] = "-";

			// 다음 위치에서 파이프라인을 놓을 수 있는지 확인
			// 놓을 수 없으면 다음 방향을 계속 검사함
			if (pipeline(nx, ny))
				return true;

		}

		// 다음 파이프라인을 놓을 수 없게 되면 백트래킹
		return false;
	}

}

// 501724KB /	1696ms
