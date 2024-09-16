class Solution {
    public boolean solution(boolean x1, boolean x2, boolean x3, boolean x4) {
        boolean answer = true;
        boolean a;
        boolean b;
        
        if (x1 == x2 && x1 == false) {
            a = false;
        } else {
            a = true;
        }
        
        if (x3 == x4 && x3 == false) {
            b = false;
        } else {
            b = true;
        }
        
        if (a == b && a == true) {
        } else {
            answer = false;
        }
        
        
        
        
        return answer;
    }
}