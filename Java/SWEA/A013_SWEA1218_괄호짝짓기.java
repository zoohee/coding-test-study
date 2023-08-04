package SWEA;

import java.io.*;
import java.util.Stack;

public class A013_SWEA1218_괄호짝짓기 {
	private static Stack<Character> stack;
	private static int check = 1;

	public static void main(String[] args) throws Exception {
		System.setIn(new FileInputStream("input013.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		stack = new Stack<Character>();
		for (int t = 1; t <= 10; t++) {
			int n = Integer.parseInt(br.readLine());
			String str = br.readLine();
			for (int i = 0; i < n; i++) {
				if (str.charAt(i) == '(' | str.charAt(i) == '{' | 
						str.charAt(i) == '[' | str.charAt(i) == '<') {
					stack.push(str.charAt(i));
				} else {
					if ((stack.peek() == '(' & str.charAt(i)==')') |
							(stack.peek() == '{' & str.charAt(i)=='}') |
							(stack.peek() == '[' & str.charAt(i)==']') |
							(stack.peek() == '<' & str.charAt(i)=='>')) {
						stack.pop();
					} else {
						check = 0;
						break;
					}
				}
			}
			System.out.println("#"+t+" "+check);
			check = 1;
		}

	}

}

// 18652kb / 106ms 
