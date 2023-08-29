package BOJ;

import java.io.*;
import java.util.*;

public class S1525_퍼즐 {
	static String correct = "123456780";
	static Map<String, Integer> map = new HashMap<>();
	static int dx[] = {1, 0, -1, 0};
	static int dy[] = {0, 1, 0, -1};
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		// 입력
		String init = "";

		for (int i=0; i<3; i++) {
			String s[] = br.readLine().split(" ");
			for(int j=0; j<3; j++) {
				init += Integer.parseInt(s[j]);
			}
		}
		
		map.put(init,  0);
		System.out.println(bfs(init));
		
	}
	
	public static int bfs(String init) {
		ArrayDeque<String> que = new ArrayDeque<String>();
		que.add(init);
		
		// 더 이상 움직일 수 없거나 0이 마지막 자리에 도착하면
		while(!que.isEmpty()) {
			String cur = que.poll();
			
			int move = map.get(cur);
			int empty = cur.indexOf('0'); // 0의 위치 반환
			int px = empty % 3;
			int py = empty / 3;
			
			if (cur.equals(correct)) return move; // 현재 위치가 123456780 이면 이동횟수 반
			
			for (int i=0; i<4; i++) {
				int nx = px + dx[i];
				int ny = py + dy[i];
				
				if (nx<0 || ny<0 || nx>2 || ny>2) continue;
				
				int nCur = ny*3 + nx;
				char ch = cur.charAt(nCur); // 이동한 위치의 문자 반환
				String next = cur.replace(ch, 'c');
				next = next.replace('0', ch);
				next = next.replace('c', '0');
				
				if(!map.containsKey(next)) { // 이동한 모양이 map에 존재하지 않으면
					que.add(next); // 큐에 삽입
					map.put(next, move+1); // map에 모양 기억
				}
			}
		}
		return -1;
	}
}
