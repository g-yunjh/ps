class Solution {
    public String solution(String code) {
        String answer = "";
        
        int mode = 0;
        for (int idx = 0; idx < code.length(); idx ++) {
            
            if (code.charAt(idx) == '1') {
                mode = (mode == 0) ? 1 : 0;
                continue;
            }
            
            if (mode == 0 && idx % 2 == 0) {
                answer += code.charAt(idx);
            } else if (mode == 1 && idx % 2 == 1) {
                answer += code.charAt(idx) ;
            }
            
        }
        
        if (answer == "") {
            answer = "EMPTY";
        }
        return answer;
    }
}