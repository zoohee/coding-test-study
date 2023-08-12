package SWEA;

import java.io.*;
import java.util.StringTokenizer;

public class _10726_이진수표현 {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());

		for (int t = 1; t <= T; t++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int n = Integer.parseInt(st.nextToken());
			int m = Integer.parseInt(st.nextToken());

			int mask = (1 << (n)) - 1; // 길이 N
			if (mask == (m & mask)) { // m&mask -> m의 마지막 n
				System.out.println("#"+t+" "+"ON");
			} else {
				System.out.println("#"+t+" "+"OFF");
			}
		}
	}

}

// 34160kb / 200ms