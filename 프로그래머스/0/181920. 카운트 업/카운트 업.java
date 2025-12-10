import java.util.ArrayList;

class Solution {
    public int[] solution(int start_num, int end_num) {
        int[] answer = {};
        
        ArrayList<Integer> list = new ArrayList<>();
        
        for (;start_num <= end_num; start_num++ ) {
            list.add(start_num);
        }
        
        
        
        answer = list.stream().mapToInt(Integer::intValue).toArray();
        return answer;
    }
}