package BOJ;

// 실행시간: 656 ms
// 메모리: 46552 KB
// 난이도: Silver 1

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class _14940_쉬운최단거리 {
    static int n, m, arr[][];
    static int[] dx = new int[] {-1, 0, 1, 0}; // 북 동 남 서
    static int[] dy = new int[] {0, 1, 0, -1};
    static boolean visited[][];
    static int ans[][], start[];
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        arr = new int[n][m];
        visited = new boolean[n][m];
        ans = new int[n][m];

        for(int i=0; i<n; i++) {
            st = new StringTokenizer(br.readLine());
            for(int j=0; j<m; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
                if(arr[i][j] == 2) {
                    start = new int[] {i, j};
                }
            }
        }

        bfs(start);

        for(int i=0; i<n; i++) {
            for(int j=0; j<m; j++) {
                if(!visited[i][j] && arr[i][j]!=0) {
                    sb.append(-1).append(" ");
                } else {
                    sb.append(ans[i][j]).append(" ");
                }
            }
            sb.append("\n");
        }

        System.out.println(sb);
    }

    public static void bfs(int[] start) {
        Queue<int[]> que = new ArrayDeque<>();
        que.add(start);
        visited[start[0]][start[1]] = true;

        while(!que.isEmpty()) {
            int[] cur = que.poll();
            int x = cur[0];
            int y = cur[1];

            for(int d=0; d<4; d++) {
                int nx = x + dx[d];
                int ny = y + dy[d];

                if(nx < 0 || nx >= n || ny < 0 || ny >= m) continue;

                if(!visited[nx][ny] && arr[nx][ny] == 1) {
                    ans[nx][ny] = ans[x][y]+1;
                    visited[nx][ny] = true;
                    que.add(new int[] {nx, ny});
                }
            }

        }
    }
}