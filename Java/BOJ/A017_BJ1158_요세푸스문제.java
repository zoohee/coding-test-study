package Java.BOJ;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class A017_BJ1158_요세푸스문제 {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		String[] s = br.readLine().split(" ");
		int n = Integer.parseInt(s[0]);
		int k = Integer.parseInt(s[1]);

		ArrayList<Integer> arr = new ArrayList<Integer>();
		for (int i=1; i<=n; i++) {
			arr.add(i);
		}
		
		sb.append("<");
		
		int current = k-1;
		while(arr.size()>0) {
			sb.append(arr.get(current)+", ");
			arr.remove(current);
			current += k-1;
			
			while (current >= arr.size() & arr.size()!=0) {
				current -= arr.size();
			}	
		}
		
		sb.deleteCharAt(sb.length()-1);
		sb.deleteCharAt(sb.length()-1);
		sb.append(">");
		
		System.out.println(sb);
		
	}

}

//1 2 3 4 5 6 7  --3
//1 2 4 5 6 7  --6
//1 2 4 5 7 --2
//1 4 5 7 --7
//1 4 5