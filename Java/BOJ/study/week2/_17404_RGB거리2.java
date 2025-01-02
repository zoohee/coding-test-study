package BOJ.study.week2;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.StringTokenizer;

public class _17404_RGB거리2 {
    static int n;
    static int[][] graph, dp;
    static List<Integer> candidates;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());
        graph = new int[n][3];
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < 3; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        candidates = new ArrayList<>();
        solve();

        System.out.print(Collections.min(candidates));
    }

    public static void solve() {

        dp = new int[n][3];
        for (int i = 0; i < 3; i++) {
            // dp 배열 초기화
            for (int j = 0; j < 3; j++) {
                if (i == j) {
                    dp[0][j] = graph[0][j];
                } else {
                    dp[0][j] = 1001;
                }
            }

            // 이전 행에서 같은 열 아닌 값 중 최소값 더함
            for (int k = 1; k < n; k++) {
                dp[k][0] = Math.min(dp[k - 1][1], dp[k - 1][2]) + graph[k][0];
                dp[k][1] = Math.min(dp[k - 1][0], dp[k - 1][2]) + graph[k][1];
                dp[k][2] = Math.min(dp[k - 1][0], dp[k - 1][1]) + graph[k][2];
                // 마지막 행에서 첫 행과 비교 후 같은 열 아닌 값만 후보에 저장
                if (k == n - 1) {
                    if (i == 0) {
                        candidates.add(Math.min(dp[n - 1][1], dp[n - 1][2]));
                    }
                    if (i == 1) {
                        candidates.add(Math.min(dp[n - 1][0], dp[n - 1][2]));
                    }
                    if (i == 2) {
                        candidates.add(Math.min(dp[n - 1][0], dp[n - 1][1]));
                    }
                }
            }
        }
    }
}

