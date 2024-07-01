package BOJ;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class _1138_한줄로서기 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] arr = new int[n+1];
        for (int i=1; i<=n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        List<Integer> result = new ArrayList<>();
        for (int i=n; i>=1; i--) {
            result.add(arr[i], i);
        }

        for (int i=0; i<n; i++) {
            System.out.print(result.get(i)+" ");
        }
    }
}
