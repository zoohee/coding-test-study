package SWEA;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class B005_SWEA9229_한빈이와SpotMart {

	public static void main(String[] args) throws Exception {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int T = Integer.parseInt(br.readLine());
		
		for(int t=1; t<=T; t++) {
			String[] s = br.readLine().split(" ");
			int n = Integer.parseInt(s[0]);
			int m = Integer.parseInt(s[1]);
			
			s = br.readLine().split(" ");
			int[] arr = new int[n];
			for(int i=0 ; i<n; i++) {
				arr[i] = Integer.parseInt(s[i]);
			}
			
			int maxWeight = -1;
			for(int i=0 ; i<n; i++) {
				for(int j=i+1; j<n; j++) {
					if(maxWeight < arr[i]+arr[j] && arr[i]+arr[j] <= m) {
						maxWeight = arr[i]+arr[j];
					}
				}
			}
			
			System.out.println("#"+t+" "+maxWeight);
		}
	}

}

