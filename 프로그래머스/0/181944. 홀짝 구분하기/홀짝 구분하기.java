import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        
        if (n%2 == 0){
            System.out.printf("%d is even", n);
        } else if (n%2 == 1){
            System.out.printf("%d is odd", n);
        }
    }
}