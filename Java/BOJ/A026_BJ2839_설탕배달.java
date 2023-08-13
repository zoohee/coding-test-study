package BOJ;

import java.util.Scanner;

public class A026_BJ2839_설탕배달 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int answer = -1;
		int cnt = 0;
		
		while(true) { 
			if(n < 0) { // 3씩 빼다가 음수가 되면 반복문 탈출하고 -1 출력
				break;
			}
			
			if(n % 5 == 0) { // 3씩 뺴다가 5의 배수가 되면 5를 제일 많이 쓰므로 최소 봉지 수
				answer = n/5 + cnt; // 5kg 봉지수 + 3kg 봉지수 출력
				break;
			}
			
			cnt++;
			n -= 3;
		}
		
		System.out.println(answer);
	}

}
