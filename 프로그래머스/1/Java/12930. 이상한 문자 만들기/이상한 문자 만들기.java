class Solution {
    public String solution(String s) {
        String answer = "";
        int wordIndex = 0;

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);

            if (c == ' ') {
                answer += " ";
                wordIndex = 0;
            } else {
                if (wordIndex % 2 == 0) {
                    answer += Character.toUpperCase(c);
                } else {
                    answer += Character.toLowerCase(c);
                }

                wordIndex++;
            }
        }

        return answer;
    }
}