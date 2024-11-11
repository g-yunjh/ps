import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt(); // 배열의 크기
        int M = sc.nextInt(); // 쿼리의 개수
        int[] arr = new int[N];
        
        // 배열 입력
        for (int i = 0; i < N; i++) {
            arr[i] = sc.nextInt();
        }

        // 누적 합 배열 생성
        int[] prefixSum = new int[N + 1]; // prefixSum[0]은 0으로 설정
        for (int i = 1; i <= N; i++) {
            prefixSum[i] = prefixSum[i - 1] + arr[i - 1];
        }

        // 쿼리 처리
        for (int i = 0; i < M; i++) {
            int num1 = sc.nextInt();
            int num2 = sc.nextInt();
            // 구간 합 계산
            int sum = prefixSum[num2] - prefixSum[num1 - 1];
            System.out.println(sum);
        }
    }
}