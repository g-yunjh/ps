import java.util.ArrayList;

class Solution {
    public int[] solution(int l, int r) {
        ArrayList<Integer> list = new ArrayList<>();        
        
        for (int i = l ; i<=r ; i++) {
            String str = Integer.toString(i);
            for (int j = 0; j < str.length() ; j++) {
                if (str.charAt(j) != '0' && str.charAt(j) != '5') {
                    break;
                }
                if (j == str.length() - 1) {
                    list.add(Integer.parseInt(str));
                }
            }                 
        }
        
        if (list.isEmpty()) {
            list.add(-1);
        }
        
        
        return list.stream().mapToInt(Integer::intValue).toArray();
    }
}