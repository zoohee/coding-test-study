package BOJ.ssafy;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

public class A027_BJ16435_스네이크버드 {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] s = br.readLine().split(" ");
		
		int n = Integer.parseInt(s[0]);
		int l = Integer.parseInt(s[1]);
		int len[] = new int[n];
		
		s = br.readLine().split(" ");
		for(int i=0; i<n; i++) {
			len[i] = Integer.parseInt(s[i]);
		}
		
		Arrays.sort(len); // 과일 높이 낮은 것부터 오름차순 정렬
		
		for(int i=0; i<n; i++) {
			if(len[i] <= l) { // 과일이 스네이크버드 길이보다 낮거나 같으면
				l++;
			} else { // 과일이 더 높아서 못 먹으면 break
				break;
			}
		}
		
		System.out.println(l); // 최대 길이 출력
		
	}

}

// 14456KB / 128ms
