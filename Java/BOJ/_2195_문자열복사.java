package BOJ;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class _2195_문자열복사 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String S = br.readLine();
        String P = br.readLine();

        int idx = 0;
        int cnt = 0;
        for (int i = 0; i < P.length(); i++) {
            String tmp = P.substring(idx, i+1);
            if (!S.contains(tmp)) { // 부분 문자열이 S에 포함되지 않으면 직전까지의 결과 저장
                cnt++;
                idx = i;
            }
            // 부분 문자열이 S에 포함되면 통과
        }
        System.out.println(cnt+1);
    }
}
