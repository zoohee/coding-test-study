package Java.SWEA;

import java.util.Scanner;

public class A001_SWEA1289_원재의메모리복구하기 {

	public static void main(String[] args) throws Exception {
		Scanner sc = new Scanner(System.in);
		int cnt = 0;
		int t = sc.nextInt();
		sc.nextLine();
		
		char init = '0';
		for (int i = 0; i < t; i++) {
			String input = sc.nextLine();
			init = '0';
			cnt = 0;
			for (int j=0; j<input.length(); j++) {
				if (input.charAt(j) != init) {
					init = input.charAt(j);
					cnt++;
				}
			}
			System.out.printf("#%d %d\n", i+1, cnt);
		}
	}
}