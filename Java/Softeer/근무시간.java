package Softeer;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class 근무시간 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int result = 0;
        for (int i=0; i<5; i++) {
            String[] line = br.readLine().split(" ");
            int start = Integer.parseInt(line[0].substring(0,2))*60 +
                    Integer.parseInt(line[0].substring(3,5));
            int end = Integer.parseInt(line[1].substring(0,2))*60 +
                    Integer.parseInt(line[1].substring(3,5));

            result += end-start;
        }
        System.out.println(result);
    }
}
