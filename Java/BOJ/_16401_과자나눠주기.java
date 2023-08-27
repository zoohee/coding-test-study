package BOJ;

import java.io.*;
import java.util.*;

public class _16401_과자나눠주기 {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		// m, n 입력
		String[] s = br.readLine().split(" ");
		int m = Integer.parseInt(s[0]);
		int n = Integer.parseInt(s[1]);
		
		// 쿠키 입력
		s = br.readLine().split(" ");
		Integer cookie[] = new Integer[n];
		for(int i=0; i<n; i++) {
			cookie[i] = Integer.parseInt(s[i]);
		}
		
		// 내림차순 정렬 (최대값 찾기)
		Arrays.sort(cookie, Collections.reverseOrder());

		int left = 1;
		int right = cookie[0];
		int result = 0;
		
        // 왼쪽 인덱스가 오른쪽 인덱스보다 커질때까지
		while(left <= right) {
			int mid = (left+right)/2; // 중간 인덱스 저장
			int cnt = 0;
			
			for (int i=0; i<n; i++) {
				cnt += cookie[i] / mid; // 중간값으로 나눈 몫 카운트
				if (cnt>=m || cookie[i] < mid) break; // 카운트가 조카수보다 커지거나 쿠키가 중간값보다 작아지면 멈춤
			}
			
			if (cnt >= m) { // 카운트가 조카수보다 커지면 값 늘려서 다시 시도
				result = mid;
				left = mid + 1;
			} else {
				right = mid - 1;
			}
		}
		
		System.out.println(result);
		
	}

}
