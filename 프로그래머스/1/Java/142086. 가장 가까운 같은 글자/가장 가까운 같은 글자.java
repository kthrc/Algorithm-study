import java.util.Arrays;

class Solution {
    public int[] solution(String s) {
        int[] answer = new int[s.length()];
        int[] last = new int[26];

        Arrays.fill(last, -1);

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            int index = c - 'a';

            if (last[index] == -1) {
                answer[i] = -1;
            } else {
                // 현재 위치 - 가장 최근에 나온 위치
                answer[i] = i - last[index];
            }

            last[index] = i;
        }

        return answer;
    }
}