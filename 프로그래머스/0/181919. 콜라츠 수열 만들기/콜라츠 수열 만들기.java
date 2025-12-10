import java.util.ArrayList;

class Solution {
    public int[] solution(int n) {
        int[] answer = {};
        
        ArrayList<Integer> list = new ArrayList<>();
        
        list.add(n);
        do {
            if (n % 2 == 0) {
                n = n / 2;
            } else if (n % 2 == 1) {
                n = 3*n + 1;
            }
            list.add(n);
        } while (n != 1) ; 
        
        
        answer = list.stream().mapToInt(Integer::intValue).toArray();
        return answer;
    }
}