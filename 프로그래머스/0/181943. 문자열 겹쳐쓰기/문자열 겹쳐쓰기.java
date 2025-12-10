class Solution {
    public String solution(String my_string, String overwrite_string, int s) {
        String answer = "";
        char a;
        
        for (int i = 0; i < s; i++) {
            a = my_string.charAt(i);
            answer += a;
        }
        
        for (int i = 0; i< overwrite_string.length(); i++) {
            a = overwrite_string.charAt(i);
            answer += a;
        }
        
        if (s + overwrite_string.length() < my_string.length()){
            for (int i = overwrite_string.length() + s; i<my_string.length(); i++) {
                a = my_string.charAt(i);
                answer += a;
                }
            }
        
        return answer;
    }
}