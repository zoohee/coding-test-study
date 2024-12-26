package BOJ.ssafy;

import java.io.*;

public class A029_BJ1074_Z {

	static int r, c, cnt, originSize;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] s = br.readLine().split(" ");
		int n = Integer.parseInt(s[0]);
		r = Integer.parseInt(s[1]);
		c = Integer.parseInt(s[2]);

		originSize = (int) Math.pow(2, n);

		Z(r, c, originSize);
		System.out.println(cnt);
	}

	private static void Z(int sr, int sc, int size) {
		if (size <= 1) {
			return;
		}

		int half = size / 2;
		
		// 찾으려 하는 위치의 사분면을 찾아 들어감
		if (sr < half && sc < half) { // 1사분면
			Z(sr, sc, half); 
		} else if (sr < half && sc >= half) { // 2사분면
			cnt += size * size / 4; // 
			Z(sr, sc - half, half);
		} else if (sr >= half && sc < half) { // 4사분면
			cnt += (size * size / 4) * 2; 
			Z(sr - half, sc, half);
		} else { // 3사분면
			cnt += (size * size / 4) * 3;
			Z(sr - half, sc - half, half); 
		}
	}
}

// 11516KB / 76ms