def solution(babbling):
    answer = 0
    sounds = ["aya", "ye", "woo", "ma"]

    for word in babbling:
        prev = ""
        i = 0

        while i < len(word):
            found = False

            for sound in sounds:
                if word.startswith(sound, i) and sound != prev:
                    prev = sound
                    i += len(sound)
                    found = True
                    break

            if not found:
                break

        if i == len(word):
            answer += 1

    return answer