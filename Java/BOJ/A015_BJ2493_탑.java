package BOJ;

import java.io.*;
import java.util.*;

public class A015_BJ2493_탑 {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		int n = Integer.parseInt(br.readLine());
		StringTokenizer st = new StringTokenizer(br.readLine());

		Stack<int[]> stack = new Stack<>();
		for (int i = 1; i <= n; i++) {
			int top = Integer.parseInt(st.nextToken());
			
			while (!stack.isEmpty()) {
				if (stack.peek()[1] >= top) {
					sb.append(stack.peek()[0] + " ");
					break;
				}
				stack.pop();
			}
			
			if (stack.isEmpty()) {
				sb.append("0 ");
			}
	
			stack.push(new int[] { i, top });
		}
		
		System.out.println(sb);
	}
}

// 101420kb / 844ms
