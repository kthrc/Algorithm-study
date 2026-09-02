import java.util.*;

class Solution {
    public int[] solution(int[] arr, int divisor) {
        ArrayList<Integer> list = new ArrayList<>();
        
        // divisor로 나누어 떨어지는 숫자만 저장
        for (int num : arr) {
            if (num % divisor == 0) {
                list.add(num);
            }
        }
        
        // 하나도 없다면 [-1]
        if (list.isEmpty()) {
            return new int[]{-1};
        }
        
        Collections.sort(list);
        
        int[] answer = new int[list.size()];
        
        for (int i = 0; i < list.size(); i++) {
            answer[i] = list.get(i);
        }
        
        return answer;
    }
}