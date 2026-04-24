def LinkingPhoneNumber(phone_cnt, phone_num):
    # 앞자리가 겹치는대로 리스트 정렬
    phone_num.sort()

    for i in range(phone_cnt - 1):
        if phone_num[i+1].startswith(phone_num[i]):
            print("NO")
            return
    print("YES")


# 테스트케이스 개수
testcase_cnt = int(input().strip())

for _ in range(testcase_cnt):
    phone_cnt = int(input().strip())
    phone_num = []
    
    for _ in range(phone_cnt):
        phone_num.append(input().strip())
    LinkingPhoneNumber(phone_cnt, phone_num)  