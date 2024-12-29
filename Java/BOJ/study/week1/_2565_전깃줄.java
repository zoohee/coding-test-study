package BOJ.study.week1;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.StringTokenizer;

public class _2565_전깃줄 {
    static int n;
    static int[] dp;
    static int[][] arr;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());

        dp = new int[n];
        arr = new int[n][2];

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            arr[i][0] = Integer.parseInt(st.nextToken());
            arr[i][1] = Integer.parseInt(st.nextToken());
        }

        // A 전봇대 기준으로 오름차순 정렬
        Arrays.sort(arr, new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                return o1[0] - o2[0];
            }
        });

        // A 전봇대의 i번째 전선 기준으로 연결가능한 최대 개수 구하기
        int max = 0;
        for (int i = 0; i < n; i++) {
            max = Math.max(recur(i), max);
        }

        System.out.println(n - max);
    }

    public static int recur(int n) {
        if (dp[n] == 0) {
            dp[n] = 1;
            for (int i = n + 1; i < dp.length; i++) {
                // A 전봇대의 N번째 전선과 연결된 B 전봇대의 위치가 i번째보다 더 앞이어야 연결 가능
                if (arr[n][1] < arr[i][1]) {
                    dp[n] = Math.max(dp[n], recur(i) + 1);
                }
            }
        }

        return dp[n];
    }
}
