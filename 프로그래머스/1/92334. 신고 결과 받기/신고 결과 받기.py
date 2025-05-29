def solution(id_list, report, k):
    count = [0] * (len(id_list))
    report_set = set(report) # 중복 제거
    report_list = list(report_set) # 중복 제거한 신고 내용
        
    blacklist = set() # set로 변경 -> 시간복잡도 O(1)
    report_count = {}
    
    
    for i in range(len(report_list)):
        reporter, reported = report_list[i].split(' ')
        
        if reported not in report_count:
            report_count[reported] = 1
        else:
            report_count[reported] += 1
    
    for item in report_count:
        if report_count[item] >= k:
            blacklist.add(item)
    
    split_report_list = [r.split(' ') for r in report_list]

    # 유저 이름 → 인덱스를 바로 찾는 딕셔너리
    id_index = {}
    for i in range(len(id_list)):
        id_index[id_list[i]] = i

    for reporter, reported in split_report_list:
        if reported in blacklist:
            count[id_index[reporter]] += 1

    return count