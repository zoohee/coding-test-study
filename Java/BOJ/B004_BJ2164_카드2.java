package BOJ;

import java.util.ArrayDeque;
import java.util.Scanner;

public class B004_BJ2164_카드2 {
	private static ArrayDeque<Integer> deque;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		deque = new ArrayDeque<>();
		
		for (int i=n; i>=1; i--) {
			deque.add(i);
		}
		
		while (deque.size() > 1) {
			deque.pollLast();
			deque.addFirst(deque.pollLast());
		}
		
		System.out.println(deque.pollFirst());
	}
}

// 32300ms / 300ms
