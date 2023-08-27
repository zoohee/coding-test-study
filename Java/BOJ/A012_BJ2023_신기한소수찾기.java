package BOJ;

import java.util.Scanner;

public class A012_BJ2023_신기한소수찾기 {
	private static int n;
	private static StringBuilder sb = new StringBuilder();
	private static Scanner sc;
	public static void main(String[] args) {
		sc = new Scanner(System.in);
		n = sc.nextInt();

		getResult(0, n);
		
		System.out.println(sb);
	}

	// 재귀로 4자리가 모두 소수인 수면 출력
	public static void getResult(int num, int n) {
		if (n==0) {
			if (isPrimeNumber(num)) { // 소수면 답 추가
				sb.append(num).append("\n");
				return;
			}
		}
		
		for(int i=0; i<10; i++) {
			int next = num*10+i; // 소수면 10곱해서 1의자리수 다 돌려봄
			if (isPrimeNumber(next)) { // 소수면 
				getResult(next, n-1); // 재귀 돌려서 답 추가
			}
		}
	}

	// 소수 찾는 함수
	public static boolean isPrimeNumber(int num) {
		if (num < 2)
			return false;

		for (int i = 2; i <= Math.sqrt(num); i++) {
			if (num % i == 0) {
				return false;
			}
		}
		return true;
	}
}
