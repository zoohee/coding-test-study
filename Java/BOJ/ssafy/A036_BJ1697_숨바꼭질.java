package BOJ.ssafy;

import java.io.*;
import java.util.*;

public class A036_BJ1697_숨바꼭질 {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] s = br.readLine().split(" ");
		int n = Integer.parseInt(s[0]);
		int k = Integer.parseInt(s[1]);
		
		Queue<Integer> que = new ArrayDeque<>();
		que.add(n);
		
		int[] list = new int[100001];
		list[n] = 0;
		
		while(!que.isEmpty()) {
			int cur = que.poll();
			
			if (cur == k) {
				System.out.println(list[k]);
				break;
			}
			
			for (int x: new int[] {cur+1, cur-1, cur*2}) {
				if(x < 0 || x > 100000) continue;
				if(list[x] > 0) continue;
				list[x] = list[cur] + 1;
				que.add(x);
			}
			
		}
	}

}

// 17644KB / 128ms