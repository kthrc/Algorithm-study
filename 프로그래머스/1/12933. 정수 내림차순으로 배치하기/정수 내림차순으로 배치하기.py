def solution(n):
    n_list = []
    n = str(n)
    n_list = list(n)
    n_list.sort(reverse=True)
    return int("".join(n_list))