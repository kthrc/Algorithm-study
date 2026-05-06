def solution(m, musicinfos):
    answer = "(None)"
    max_time = -1

    def change_sharp(s):
        return (s.replace("C#", "c")
                 .replace("D#", "d")
                 .replace("F#", "f")
                 .replace("G#", "g")
                 .replace("A#", "a")
                 .replace("B#", "b"))

    def to_min(t):
        h, m = map(int, t.split(":"))
        return h * 60 + m

    m = change_sharp(m)

    for info in musicinfos:
        start, end, title, melody = info.split(",")

        play_time = to_min(end) - to_min(start)
        melody = change_sharp(melody)

        played = (melody * (play_time // len(melody) + 1))[:play_time]

        if m in played and play_time > max_time:
            answer = title
            max_time = play_time

    return answer