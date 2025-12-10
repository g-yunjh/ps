class Solution {
    public int solution(int a, int b) {
        int answer = 0;
        
        String result1 =  Integer.toString(a) + Integer.toString(b);
        String result2 = Integer.toString(b) + Integer.toString(a);
        
        if (Integer.parseInt(result1) > Integer.parseInt(result2)) {
            answer = Integer.parseInt(result1);
        } else {
            answer = Integer.parseInt(result2);
        }

        
        return answer;
    }
}