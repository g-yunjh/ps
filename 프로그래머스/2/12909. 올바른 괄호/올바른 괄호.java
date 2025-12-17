import java.util.Stack;

import javax.lang.model.element.Element;

class Solution {
    boolean solution(String s) {
        Stack<Integer> stack = new Stack<>(); //push, pop, peek, empty, seach 지원
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '(') {
                stack.push(1);
            } else {
                if (stack.empty()) {
                    return false;
                } else {
                    stack.pop();
                }
            }
        }
        if (stack.empty()) {
            return true;
        } else {
            return false;
        }
    }
}