package SWEA;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class _1288_새로운불면증치료법 {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int T = Integer.parseInt(br.readLine());
		for (int t = 1; t <= T; t++) {
			int n = Integer.parseInt(br.readLine());
			int chk = 0;
			for (int k = 1;; k++) {
				int num = k * n;
				while (num > 0) {
					int digit = num % 10;
					chk |= 1 << digit;
					num /= 10;
				}

				if (chk == 0b1111111111) {
					System.out.println("#"+t+" "+k * n);
					break;
				}
			}
		}

	}
}

// 18428kb / 100ms