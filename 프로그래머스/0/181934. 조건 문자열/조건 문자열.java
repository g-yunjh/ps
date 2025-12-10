class Solution {
    public int solution(String ineq, String eq, int n, int m) {
        int answer = 0;
        
if ("<".equals(ineq) && "=".equals(eq)) {
            if (n <= m) {
                answer = 1;
            }
        } else if ("<".equals(ineq) && "!".equals(eq)) {
            if (n < m) {
                answer = 1;
            }
        } else if (">".equals(ineq) && "=".equals(eq)) {
            if (n >= m) {
                answer = 1;
            }
        } else {
            if (n > m) {
                answer = 1;
            }
        }
        
        
        
        return answer;
    }
}