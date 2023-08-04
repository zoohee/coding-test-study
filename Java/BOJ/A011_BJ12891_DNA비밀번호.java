package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashMap;

public class A011_BJ12891_DNA비밀번호 {
	private static int s, p, originCond[], answer;
	private static String password;
	private static HashMap<Character, Integer> hm = new HashMap<Character, Integer>();
	private static char[] dna = { 'A', 'C', 'G', 'T' };

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] str = br.readLine().split(" ");

		s = Integer.parseInt(str[0]);
		p = Integer.parseInt(str[1]);

		password = br.readLine();
		str = br.readLine().split(" ");

		originCond = new int[4];
		for (int i = 0; i < 4; i++) {
			originCond[i] = Integer.parseInt(str[i]);
			hm.put(dna[i], 0);
		}

		for (int i = 0; i < p; i++) {
			char ch = password.charAt(i);
			hm.put(ch, hm.get(ch) + 1);
		}
		
		if (isFull())
			answer++;

		for (int i = 1; i < s - p + 1; i++) {
			char ch = password.charAt(i-1);
			hm.put(ch, hm.get(ch) - 1);
			ch = password.charAt(i + p - 1);
			hm.put(ch, hm.get(ch) + 1);
			if (isFull())
				answer++;
		}

		System.out.println(answer);
	}

	public static boolean isFull() {
		int index = 0;
		for (char c : dna) {
			if (hm.get(c) < originCond[index]) {
				return false;
			}
			index++;
		}
		return true;
	}
}
