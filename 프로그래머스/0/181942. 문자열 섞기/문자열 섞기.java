class Solution {
    public String solution(String str1, String str2) {
        String answer = "";
        char a;
        
        for(int i = 0; i<str1.length(); i++) {
            a = str1.charAt(i);
            answer += a;
            a = str2.charAt(i);
            answer += a;
        }
        
        return answer;

    }
}