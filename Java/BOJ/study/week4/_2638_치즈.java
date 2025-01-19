package BOJ.study.week4;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class _2638_치즈 {
    static int[][] graph, air;
    static int[] dx = {0, 0, 1, -1};
    static int[] dy = {1, -1, 0, 0};
    static int n, m, cheese, answer = 0;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        graph = new int[n][m];
        cheese = 0;
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
                if (graph[i][j] == 1) {
                    cheese++;
                }
            }
        }

        while(cheese != 0) {
            bfs();
        }

        System.out.println(answer);
    }

    public static void bfs() {
        air = new int[n][m];
        Queue<Point> que = new ArrayDeque<>();
        que.add(new Point(0, 0));
        air[0][0] = -1;
        
        while (!que.isEmpty()) {
            Point cur = que.poll();

            for (int d = 0; d < 4; d++) {
                int nx = cur.x + dx[d];
                int ny = cur.y + dy[d];

                if (nx < 0 || nx >= n || ny < 0 || ny >= m) {
                    continue;
                }

                // 치즈가 있으면 공기와 접촉
                if (graph[nx][ny] == 1) {
                    air[nx][ny]++;
                }

                // 치즈가 아니고 방문한 적 없으면 방문처리
                if (graph[nx][ny] == 0 && air[nx][ny] == 0) {
                    air[nx][ny] = -1;
                    que.add(new Point(nx, ny));
                }
            }
        }

        // 2면 이상 공기 접촉하면 치즈 줄어들게 하기
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (air[i][j] >= 2) {
                    cheese--;
                    graph[i][j] = 0;
                }
            }
        }

        answer++;
    }
}

class Point {
    public int x, y;

    Point(int x, int y) {
        this.x = x;
        this.y = y;
    }
}
