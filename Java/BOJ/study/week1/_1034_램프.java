package BOJ.study.week1;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashMap;

public class _1034_램프 {
    static int n, m, k, zero, answer = 0;
    static String[] arr;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] size = br.readLine().split(" ");
        n = Integer.parseInt(size[0]);
        m = Integer.parseInt(size[1]);

        arr = new String[n];
        for (int i = 0; i < n; i++) {
            arr[i] = br.readLine();
        }

        k = Integer.parseInt(br.readLine());
        HashMap<String, Integer> map = new HashMap<>();
        for (int i = 0; i < n; i++) {
            zero = 0;
            for (int j = 0; j < m; j++) {
                // 해당 행의 0 개수 체크
                if (arr[i].charAt(j) == '0') zero++;
            }

            // 스위치 횟수 k가 zero보다 크거나 같아야 해당 행의 모든 램프 켜기 가능
            // k와 0의 개수가 짝수면 짝수, 홀수면 홀수로 일치해야 함
            if (zero <= k && zero % 2 == k % 2) {
                // 가장 많이 등장한 패턴의 횟수 업데이트
                map.put(arr[i], map.getOrDefault(arr[i], 0) + 1);
                if (map.get(arr[i]) > answer) {
                    answer = map.get(arr[i]);
                }
            }
        }

        System.out.println(answer);
    }
}
