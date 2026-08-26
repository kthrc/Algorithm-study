def solution(keymap, targets):
    answer = []
    min_press = {}

    for key in keymap:
        for i, char in enumerate(key):
            press = i + 1

            if char not in min_press:
                min_press[char] = press
            else:
                min_press[char] = min(min_press[char], press)

    for target in targets:
        total = 0

        for char in target:
            if char not in min_press:
                total = -1
                break

            total += min_press[char]

        answer.append(total)

    return answer