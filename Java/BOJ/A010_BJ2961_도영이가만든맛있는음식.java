package Java.SWEA;

import java.util.Scanner;

public class A010_BJ2961_도영이가만든맛있는음식 {

	static int N, taste[][], minTaste;
	static boolean[] isSelected;

	public static void main(String[] args) throws Exception {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		
		taste = new int[N][2];
		isSelected = new boolean[N];
		minTaste = Integer.MAX_VALUE;
		
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < 2; j++) {
				taste[i][j] = sc.nextInt();
			}
		}
		
		subset(0, 1, 0, 0);
		System.out.println(minTaste);

	}

	private static void subset(int cnt, int sour, int bitter, int selectedCount) {
		if (cnt == N) {
			if (Math.abs(sour - bitter) < minTaste && selectedCount > 0) {
				minTaste = Math.abs(sour - bitter);
			}
			return;
		}

		isSelected[cnt] = true;
		subset(cnt + 1, sour*taste[cnt][0], bitter+taste[cnt][1], selectedCount+1);
		isSelected[cnt] = false;
		subset(cnt + 1, sour, bitter, selectedCount);
	}
}
