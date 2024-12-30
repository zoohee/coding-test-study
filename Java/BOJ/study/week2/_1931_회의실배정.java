package BOJ.study.week2;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class _1931_회의실배정 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[][] meetings = new int[n][2];

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            meetings[i][0] = Integer.parseInt(st.nextToken());
            meetings[i][1] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(meetings, (a, b) -> {
            if (a[1] == b[1]) {
                return Integer.compare(a[0], b[0]); // 종료 시간이 같으면 시작 시간 기준 정렬
            }
            return Integer.compare(a[1], b[1]); // 종료 시간 기준 정렬
        });

        int count = 0;
        int currentEndTime = 0;
        for (int i = 0; i < n; i++) {
            if (currentEndTime <= meetings[i][1] && meetings[i][0] >= currentEndTime) {
                currentEndTime = meetings[i][1];
                count++;
            }
        }

        System.out.println(count);

//        for (int[] meeting : meetings) {
//            System.out.println(meeting[0] + " " + meeting[1]);
//        }

//        1 4
//        3 5
//        0 6
//        5 7
//        3 8
//        5 9
//        6 10
//        8 11
//        8 12
//        2 13
//        12 14
    }
}
