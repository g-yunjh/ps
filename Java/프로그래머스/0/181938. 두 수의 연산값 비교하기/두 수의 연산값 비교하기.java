class Solution {
    public int solution(int a, int b) {
        int answer = 0;
        
        int plus = Integer.parseInt(Integer.toString(a) + Integer.toString(b));
        int gop = 2*a*b;
        
        if (plus > gop) {
            answer = plus;
        } else {
            answer = gop;
        }
        
        
        
        return answer;
    }
}