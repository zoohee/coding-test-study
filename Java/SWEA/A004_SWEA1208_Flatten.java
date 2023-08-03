package Java.SWEA;

import java.io.*;
import java.util.*;

public class A004_SWEA1208_Flatten {

	public static void main(String[] args) throws Exception {
		// System.setIn(new FileInputStream("input004.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		for (int i = 0; i < 10; i++) {
			int dump = Integer.parseInt(br.readLine());
			String[] boxLine = br.readLine().split(" ");
			
			Integer[] arr = new Integer[100];
			
			for (int j=0; j<100; j++) {
				arr[j] = Integer.parseInt(boxLine[j]);
			}

			Arrays.sort(arr);
			while(true) {
				if (dump==0) {
					System.out.println("#"+(i+1)+" "+(arr[arr.length-1]-arr[0]));
					break;
				}
				arr[0]++;
				arr[arr.length-1]--;
				dump--;
				Arrays.sort(arr);
			}
		}
	}
}