package BOJ.study.week3;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class _13975_파일합치기3 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int t = Integer.parseInt(br.readLine());
        for (int i = 0; i < t; i++) {
            int n = Integer.parseInt(br.readLine());
            StringTokenizer st = new StringTokenizer(br.readLine());
            PriorityQueue<Long> que = new PriorityQueue<>();
            for (int j = 0; j < n; j++) {
                que.add(Long.parseLong(st.nextToken()));
            }

            Long sum = 0L;
            while (que.size() > 1) {
                Long a = que.poll();
                Long b = que.poll();

                sum += a+b;
                que.add(a+b);
            }
            System.out.println(sum);
        }
    }
}
