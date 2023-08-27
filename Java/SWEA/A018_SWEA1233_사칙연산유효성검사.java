package SWEA;

import java.io.*;
import java.util.*;

public class A018_SWEA1233_사칙연산유효성검사 {

	public static void main(String[] args) throws Exception {
		System.setIn(new FileInputStream("input018.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		for (int t = 1; t <= 10; t++) {
			int n = Integer.parseInt(br.readLine());
			Tree tree = new Tree(n);
			for (int i = 0; i < n; i++) {
				String[] s = br.readLine().split(" ");
				tree.add(s[1]);
			}
			System.out.println("#"+t+" "+tree.bfs());
		}
	}

}

class Tree<T> {
	private Object[] nodes;
	private int lastIndex = 0;
	private final int SIZE;

	public Tree(int size) {
		this.SIZE = size;
		nodes = new Object[size + 1];
	}

	public boolean isEmpty() {
		return lastIndex == 0;
	}

	public boolean isFull() {
		return lastIndex == SIZE;
	}

	public boolean add(T data) {
		if (isFull())
			return false;
		nodes[++lastIndex] = data;
		return true;
	}

	public int bfs() {
		if (isEmpty())
			return 1;
		// 탐색 순서를 관리할 대기열 자료구조 생성
		Queue<Integer> que = new ArrayDeque(); // 인덱스이므로 Integer
		// 탐색 시작의 대상부터 큐에 넣기
		que.offer(1); // 루트노드 인덱스

		while (!que.isEmpty()) {
			int current = que.poll(); // 탐색 대상 큐에서 꺼내기
			// 탐색대상 방문
	
			// 현재 탐색 대상을 통해 탐색해야할 새로운 대상을 큐에 넣기
			if (current * 2 <= lastIndex)
				que.offer(current * 2); // 존재하므로 삽입
			if (current * 2 + 1 <= lastIndex)
				que.offer(current * 2 + 1); // 존재하므로 삽입
			if (current * 2 > lastIndex) {
				if (nodes[current].equals("-") || nodes[current].equals("+") ||
						nodes[current].equals("*") || (String)nodes[current] == "/")
					return 0;
			}
		}
		
		return 1;
	}
}