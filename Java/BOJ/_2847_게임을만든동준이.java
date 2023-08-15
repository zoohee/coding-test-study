package BOJ;

import java.io.*;

public class _2847_게임을만든동준이 {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		int[] level = new int[T];
		for(int t=0; t<T; t++) {
			level[t] = Integer.parseInt(br.readLine());
		}
		
		int cnt = 0;
		for(int i=T-1; i>0; i--) {
			if(level[i] <= level[i-1]) {
				cnt +=  level[i-1] - level[i] + 1;
				level[i-1] = level[i] - 1;
			}
		}
		
		System.out.println(cnt);
	}
}
