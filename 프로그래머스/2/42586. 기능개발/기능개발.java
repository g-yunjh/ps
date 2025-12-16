import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        // 1. 각 기능별 완료까지 걸리는 일수를 저장할 큐 (FIFO 구조)
        Queue<Integer> daysQueue = new LinkedList<>();

        // 2. 각 기능이 완료되는 데 필요한 최소 일수를 계산하여 큐에 추가
        for (int i = 0; i < progresses.length; i++) {
            int remainingProgress = 100 - progresses[i];
            int speed = speeds[i];

            // 필요한 일수 계산 (정수 나눗셈 후 올림 처리)
            // (a + b - 1) / b 는 a/b의 올림과 동일합니다.
            int requiredDays = (int) Math.ceil((double) remainingProgress / speed);
            
            daysQueue.offer(requiredDays);
        }

        // 3. 배포 결과를 저장할 리스트
        List<Integer> deployCounts = new ArrayList<>();

        // 4. 큐가 빌 때까지 배포 단위 계산
        while (!daysQueue.isEmpty()) {
            // 현재 배포될 기능의 최대 소요 일수 (가장 먼저 배포될 기능의 소요 일수)
            int maxDays = daysQueue.poll();
            
            // 이번 배포에서 함께 나갈 기능의 개수 (최소 1개)
            int count = 1;

            // 다음 기능들을 확인하며 함께 배포될 수 있는지 검사
            // 즉, 다음 기능의 소요 일수가 maxDays보다 작거나 같은지 확인
            while (!daysQueue.isEmpty() && daysQueue.peek() <= maxDays) {
                daysQueue.poll(); // 함께 배포되므로 큐에서 제거
                count++;
            }

            // 하나의 배포 단위가 완성되었으므로 개수를 리스트에 추가
            deployCounts.add(count);
        }

        // 5. 결과를 int[] 배열로 변환하여 반환
        int[] answer = new int[deployCounts.size()];
        for (int i = 0; i < deployCounts.size(); i++) {
            answer[i] = deployCounts.get(i);
        }

        return answer;
    }
}