import java.util.*;
import static java.util.stream.Collectors.*;

class Solution {
    public int solution(String[][] clothes) {
        return Arrays.stream(clothes)
                .collect(groupingBy(c -> c[1], counting())) // 종류별로 그룹화해서 개수 세기
                .values().stream()
                .reduce(1L, (ans, cnt) -> ans * (cnt + 1), (a, b) -> a * b).intValue() - 1;
    }
}