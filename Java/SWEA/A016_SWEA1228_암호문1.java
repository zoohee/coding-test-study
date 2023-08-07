package Java.SWEA;

import java.io.*;
import java.util.*;

public class A016_SWEA1228_암호문1 {

	public static void main(String[] args) throws Exception {
		System.setIn(new FileInputStream("input016.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb= new StringBuilder();
		
		for (int t = 1; t <= 10; t++) {
			int n = Integer.parseInt(br.readLine());
			String[] password = br.readLine().split(" ");

			List<String> list = new LinkedList<>(Arrays.asList(password));

			int m = Integer.parseInt(br.readLine());
			String[] orders = br.readLine().split("I ");

			for (int i = 1; i <= m; i++) {
				String[] order = orders[i].split(" ");
				int start = Integer.parseInt(order[0]);

				for (int j = 2; j < 2 + Integer.parseInt(order[1]); j++) {
					list.add(start++, order[j]);
				}
			}

			sb.append("#"+t+" ");
			for (int i = 0; i < 10; i++) {
				sb.append(list.get(i)+" ");
			}
			sb.append("\n");
		}
		
		System.out.println(sb);
	}

}
