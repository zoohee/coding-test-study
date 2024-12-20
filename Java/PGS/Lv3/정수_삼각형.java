package PGS.Lv3;

public class 정수_삼각형 {
    public int solution(int[][] triangle) {

        int n = triangle.length;
        for (int i = 1; i < n; i++) {
            for (int j = 0; j < triangle[i].length; j++) {
                if (j == 0) {
                    triangle[i][j] += triangle[i - 1][j];
                } else if (j == i) {
                    triangle[i][j] += triangle[i - 1][j - 1];
                } else {
                    triangle[i][j] += Math.max(triangle[i - 1][j], triangle[i - 1][j - 1]);
                }
            }
        }

        int answer = 0;
        for (int value : triangle[n - 1]) {
            answer = Math.max(answer, value);
        }

        return answer;
    }
}
