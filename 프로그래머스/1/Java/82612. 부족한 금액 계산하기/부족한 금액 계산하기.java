class Solution {
    public long solution(int price, int money, int count) {
        long answer = money;

        for (int i = 0; i < count; i++) {
            answer -= (long) price * (i + 1);
        }

        return answer < 0 ? -answer : 0;
    }
}