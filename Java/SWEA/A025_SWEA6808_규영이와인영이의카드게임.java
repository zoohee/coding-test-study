package SWEA;

import java.io.*;
import java.util.*;

public class A025_SWEA6808_규영이와인영이의카드게임 {

	static int win, maxScore=171, score, result[];
	static boolean visited[], check[];
	static ArrayList<Integer> ky, iy;

	public static void main(String[] args) throws Exception {
		System.setIn(new FileInputStream("input025.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int T = Integer.parseInt(br.readLine());
		for (int t = 1; t <= T; t++) {
			ky = new ArrayList<>();
			iy = new ArrayList<>();
			check = new boolean[19];
			result = new int[9];
			String s[] = br.readLine().split(" ");
			// 규영이 카드
			for (int i = 0; i < 9; i++) {
				ky.add(Integer.parseInt(s[i]));
				check[Integer.parseInt(s[i])] = true;
			}

			// 인영이 카드 구하기
			for (int i = 1; i <= 18; i++) {
				if (!check[i]) {
					iy.add(i);
				}
			}
			
			game(0, 0);
			
			System.out.println("#"+t+" "+(362880-win)+" "+win);
			win = 0;
		}
	}

	public static void game(int cnt, int flag) {
		if (cnt==9) { // 9개의 순열을 구했을 때
			int iScore = 0; // 인영이 점수 구함
			for (int i=0; i<9; i++) {
				if (result[i] > ky.get(i)) { // 인영이가 규영이보다 카드 숫자가 크면
					iScore += result[i] + ky.get(i); // 인영이한테 점수 획득
				}
				if (iScore > maxScore/2) { // 인영이 점수가 최대절반보다 커지면
					win += 1; // 인영이 승리 획득
					break;
				}
			}
			return;
		}
		
		for (int i = 0; i < 9; i++) {
            if ((flag & 1 << i) != 0)
                continue;
            
            result[cnt] = iy.get(i);
            game(cnt + 1, flag | 1 << i);
        }
		
	}
}

// 21140kb / 2795ms
