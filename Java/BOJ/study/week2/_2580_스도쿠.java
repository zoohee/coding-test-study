package BOJ.study.week2;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class _2580_스도쿠 {
    static int[][] sudoku;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        sudoku = new int[9][9];
        for (int i = 0; i < 9; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < 9; j++) {
                sudoku[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        if (solve(0, 0)) {
            for (int i = 0; i < 9; i++) {
                for (int j = 0; j < 9; j++) {
                    System.out.print(sudoku[i][j] + " ");
                }
                System.out.println();
            }
        }
    }

    public static boolean solve(int row, int col) {
        // 마지막 칸이면 종료
        if (row == 9) {
            return true;
        }

        int nextRow = (col == 8) ? row + 1 : row;
        int nextCol = (col == 8) ? 0 : col + 1;

        // 0 아니면 다음 칸으로 이동
        if (sudoku[row][col] != 0) {
            return solve(nextRow, nextCol);
        }

        for (int num = 1; num <= 9; num++) {
            if (isValid(row, col, num)) {
                sudoku[row][col] = num; // 숫자 넣기
                if (solve(nextRow, nextCol)) {
                    return true;
                }
                sudoku[row][col] = 0; // 되돌리기
            }
        }

        return false;
    }

    public static boolean isValid(int row, int col, int value) {
        // 행 체크
        for (int j = 0; j < 9; j++) {
            if (sudoku[row][j] == value) {
                return false;
            }
        }

        // 열 체크
        for (int i = 0; i < 9; i++) {
            if (sudoku[i][col] == value) {
                return false;
            }
        }

        // 박스 체크
        int box_row = (row / 3) * 3;
        int box_col = (col / 3) * 3;

        for (int i = box_row; i < box_row + 3; i++) {
            for (int j = box_col; j < box_col + 3; j++) {
                if (sudoku[i][j] == value) {
                    return false;
                }
            }
        }

        return true;
    }
}
