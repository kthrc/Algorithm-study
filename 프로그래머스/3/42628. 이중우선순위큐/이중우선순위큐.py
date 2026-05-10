def solution(operations):
    queue = []

    for oper in operations:
        cmd, num = oper.split()
        num = int(num)

        if cmd == 'I':
            queue.append(num)

        elif cmd == 'D' and queue:

            if num == 1:
                queue.remove(max(queue))

            else:
                queue.remove(min(queue))

    if not queue:
        return [0, 0]

    return [max(queue), min(queue)]