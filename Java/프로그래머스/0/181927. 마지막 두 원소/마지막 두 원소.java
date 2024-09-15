import java.util.*;

class Solution {
    public List solution(int[] num_list) {
        List<Integer> answer = new ArrayList<>();
        int last = num_list.length - 1;
        
        for (int i = 0 ; i < num_list.length; i++) {
            answer.add(num_list[i]);
        }
        
        if (num_list[last] > num_list[last-1]) {
            answer.add(num_list[last] - num_list[last-1]);
        } else {
            answer.add(num_list[last] * 2);
        }
        
        return answer;
    }
}