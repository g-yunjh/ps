class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        int[] answer = {};
        
        for (int i = 0 ; i<queries.length ; i ++) {
            int a = arr[queries[i][0]];
            int b = arr[queries[i][1]];
            
            arr[queries[i][0]] = b;
            arr[queries[i][1]] = a;
        }
        
        answer = arr;
        
        
        return answer;
    }
}