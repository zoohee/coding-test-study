package Java.BOJ;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Iterator;

public class B001_BJ1244_스위치켜고끄기 {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());

		int[] arr = new int[n];
		String[] s = br.readLine().split(" ");

		for (int i = 0; i < n; i++) {
			arr[i] = Integer.parseInt(s[i]);
		}
		n -= 1;

		int m = Integer.parseInt(br.readLine());
		for (int i = 0; i < m; i++) {
			s = br.readLine().split(" ");
			int sex = Integer.parseInt(s[0]);
			int num = Integer.parseInt(s[1]);

			switch (sex) {

			case 1: {
				for (int j = num - 1; j < arr.length; j += num) {
					if (arr[j] == 1) {
						arr[j] = 0;
					} else {
						arr[j] = 1;
					}
				}
				break;
			}

			case 2: {
				num -= 1;
				if (arr[num] == 1) {
					arr[num] = 0;
				} else {
					arr[num] = 1;
				}

				int left = num - 1;
				int right = num + 1;
				while (true) {
					if (left < 0 | right >= arr.length) {
						break;
					}

					if (arr[left] == arr[right]) {
						if (arr[left] == 1) {
							arr[left] = 0;
							arr[right] = 0;
						} else {
							arr[left] = 1;
							arr[right] = 1;
						}
					} else {
						break;
					}
					left--;
					right++;
				}
			}

			}
		}
		
		for(int i=0; i<arr.length; i++) {
			if(i>0 & i%20==0) {
				System.out.println();
			}
			System.out.print(arr[i]+" ");
		}
	}

}
