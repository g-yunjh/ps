import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        long[] sum = new long[N];
        long[] arr = new long[M];
        long answer = 0;

        // 합 배열 생성
        sum [0] = sc.nextInt();
        for (int i = 1; i < N; i++) {
            sum[i] = sum[i-1] + sc.nextInt(); 
        }

        for (int i = 0; i < N; i++) {
            int remainder = (int) (sum[i] % M);
            if (remainder == 0) {
                answer++;
            }
            arr[remainder] ++;
        }
        for (int i = 0; i < M; i++) {
            if (arr[i] > 1) {
                answer = answer + (arr[i] * (arr[i] - 1) / 2);
            }
        }
        System.out.println(answer);
    }
}