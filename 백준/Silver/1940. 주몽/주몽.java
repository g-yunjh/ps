import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        int[] A = new int[N];
        int count = 0;

        // 배열 A 입력 받기
        for (int i = 0 ; i < N ; i++) {
            A[i] = sc.nextInt();
        }

        // 두 수의 합이 M이 되는 경우를 찾는 반복문
        for (int i = 0; i < N; i++) {
            for (int j = i + 1; j < N; j++) { // j는 i + 1부터 시작
                if (A[i] + A[j] == M) {
                    count++;
                }
            }
        }

        // 결과 출력
        System.out.println(count);
    }
}
