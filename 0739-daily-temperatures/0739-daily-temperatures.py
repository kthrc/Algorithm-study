class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        answer = [0] * len(temperatures)
        index = []

        for i in range(len(temperatures)):

            while index and temperatures[index[-1]] < temperatures[i]:
                
                prev = index.pop()
                answer[prev] = i - prev # 차이 계산

            # 인덱스 추가
            index.append(i)
        
        return answer

            

