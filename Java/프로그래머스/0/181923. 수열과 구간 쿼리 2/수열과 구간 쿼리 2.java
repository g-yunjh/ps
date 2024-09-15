class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        int[] answer = new int[queries.length];

        
        for (int i = 0 ; i < queries.length ; i ++) {
            int temp = 1000001;
            int s = queries[i][0];
            int e = queries[i][1];
            int k = queries[i][2];
            
            for (; s <= e; s++) {
                if(arr[s] > k) {
                    if (arr[s] < temp) {
                        temp = arr[s];
                    }
                }
            }
            if (temp == 1000001){
                temp = -1;
            }
            answer[i] = temp;
        }
        
        return answer;
    }
}