import java.util.*;

class Solution {
    public int solution(int[] nums) {
        Arrays.sort(nums);
        
        int cnt = 0;
        int tmp = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != tmp) {
                cnt += 1;
                tmp = nums[i];
            }
        }
        if (cnt >= nums.length/2) {
            return nums.length/2;
        } else {
            return cnt;
        }
    }
}