package Softeer;
import java.io.*;
import java.util.*;

public class 금고털이 {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int w = Integer.parseInt(st.nextToken());
        int n = Integer.parseInt(st.nextToken());

        int[][] arr = new int[n][2];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());

            arr[i][0] = Integer.parseInt(st.nextToken());
            arr[i][1] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(arr, (o1, o2) -> {
            return o2[1]-o1[1];
        });

        int result = 0;

        for (int i=0; i<n; i++) {
            if (w <= arr[i][0]) {
                result += w * arr[i][1];
                break;
            } else {
                result += arr[i][0] * arr[i][1];
                w -= arr[i][0];
            }
        }

        System.out.println(result);
    }
}