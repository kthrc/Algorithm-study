class Solution {
    public int[] solution(int[] arr) {
        // 원소가 하나뿐이면 제거 후 빈 배열이 되므로 [-1]
        if (arr.length == 1) {
            return new int[]{-1};
        }

        // 최솟값 찾기
        int min = arr[0];

        for (int i = 1; i < arr.length; i++) {
            if (arr[i] < min) {
                min = arr[i];
            }
        }

        // 최솟값을 제외하므로 크기는 기존보다 1 작음
        int[] answer = new int[arr.length - 1];
        int index = 0;

        // 최솟값이 아닌 값만 answer에 넣기
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] != min) {
                answer[index] = arr[i];
                index++;
            }
        }

        return answer;
    }
}