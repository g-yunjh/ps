import java.util.Scanner;
import java.util.Arrays;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] arr = new int[N];

        // 배열 입력 받기
        for (int i = 0 ; i < N ; i++) {
            arr[i] = sc.nextInt();
        }

        // sort the array
        Arrays.sort(arr);
        // 좋은 수인지 판단하기
        int count = 0;
        for(int k = 0; k < N ; k++) {
            int i = 0;
            int j = N-1;
            while (i < j) {
                if (arr[k] == arr[i] + arr[j]){
                    if (i != k && j != k){
                        count++;
                        break;
                    } else if (i==k) {
                        i++;
                    } else if (j==k) {
                        j--;
                    }
                } else if (arr[i] + arr[j] < arr[k]) {
                    i++;
                } else {
                    j--;
                }
            }
        }

        // 최종 출력
        System.out.println(count);
    }
}