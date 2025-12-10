import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt(); // 행렬의 크기 N x N
        int M = sc.nextInt(); // 쿼리의 개수 M
        int A[][] = new int[N + 1][N + 1]; // 1-based index를 사용하기 위해 크기를 N+1로 설정

        // 행렬 A 입력 (1-based index)
        for (int i = 1; i <= N; i++) {
            for (int j = 1; j <= N; j++) {
                A[i][j] = sc.nextInt();
            }
        }

        // 2차원 누적 합 배열 생성
        int sum[][] = new int[N + 1][N + 1];

        // 누적 합 계산
        for (int i = 1; i <= N; i++) {
            for (int j = 1; j <= N; j++) {
                sum[i][j] = A[i][j] + sum[i - 1][j] + sum[i][j - 1] - sum[i - 1][j - 1];
            }
        }

        // 쿼리 처리
        for (int i = 0; i < M; i++) {
            int n1 = sc.nextInt(); // 시작 행 번호
            int n2 = sc.nextInt(); // 시작 열 번호
            int n3 = sc.nextInt(); // 끝 행 번호
            int n4 = sc.nextInt(); // 끝 열 번호

            // 구간 합 계산
            int mSum = sum[n3][n4] - sum[n1 - 1][n4] - sum[n3][n2 - 1] + sum[n1 - 1][n2 - 1];
            System.out.println(mSum);
        }
    }
}