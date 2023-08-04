package SWEA;

import java.io.*;
import java.util.ArrayDeque;

public class A014_SWEA1225_암호생성기 {
	private static ArrayDeque<Integer> deque;
	private static String str[];
	private static int cnt;

	public static void main(String[] args) throws Exception {
		System.setIn(new FileInputStream("input014.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		for (int t = 1; t <= 10; t++) {
			cnt = 1;
			br.readLine();
			str = br.readLine().split(" ");
			deque = new ArrayDeque<>();
			
			for (int i = 0; i < 8; i++) {
				deque.addLast(Integer.parseInt(str[i]));
			}

			while (true) {
				if (deque.getLast() <= 0) {
					deque.pollLast();
					deque.addLast(0);
					System.out.print("#" + t + " ");
					for (int i = 0; i < 8; i++) {
						System.out.print(deque.pollFirst() + " ");
					}
					System.out.println();
					break;
				}

				deque.addLast(deque.pollFirst() - cnt);
				cnt++;
				if (cnt == 6) {
					cnt = 1;
				}
			}
		}
	}
}

// 20484kb / 132ms
