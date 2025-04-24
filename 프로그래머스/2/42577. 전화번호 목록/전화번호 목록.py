def solution(phone_book):
    phone_book.sort()  # 정렬하면 접두사들은 인접하게 됨
    for i in range(len(phone_book) - 1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    return True