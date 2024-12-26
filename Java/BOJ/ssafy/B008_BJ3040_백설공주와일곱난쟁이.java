package BOJ.ssafy;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class B008_BJ3040_백설공주와일곱난쟁이 {

	static int[] hat;
	static boolean[] visited;
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		hat = new int[9];
		for (int i=0; i<9; i++) {
			hat[i] = Integer.parseInt(br.readLine());
		}
		
		visited = new boolean[9];
		combination(hat, visited, 0, 7);
		
	}
	
	static void combination(int[] arr, boolean[] visited, int start, int r) {
	    if(r == 0) {
	    	int cnt = 0;
	    	for (int i=0; i<9; i++) { 
	    		if (visited[i] == true) { // 조합으로 선택된 원소면
	    			cnt += arr[i]; // 모자 번호 카운트
	    		}
	    	}
	    	if (cnt == 100) { // 카운트 합이 100이면 일곱 난쟁이
	    		for (int i=0; i<9; i++) {
		    		if (visited[i] == true) {
		    			System.out.println(arr[i]); // 난쟁이 번호 출력
		    		}
		    	}
	    		System.exit(0); // 출력 후 프로그램 종료
	    	}
	    	cnt = 0;
	        return;
	    } 

	    for(int i=start; i<9; i++) {
	        visited[i] = true;
	        combination(arr, visited, i + 1, r - 1);
	        visited[i] = false;
	    }
	}
}
