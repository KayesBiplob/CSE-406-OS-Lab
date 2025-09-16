requests = [14, 20, 29, 40, 50, 110]
head = 29
direction = "left"

def scan(requests, head, direction):
    requests.sort()

    left = [r for r in requests if r<head]
    right = [r for r in requests if r>head]

    sequence = [head]
    total_seek = 0
    current = head

    if direction == "left":
        for r in reversed(left):
            total_seek += abs(current - r)
            current = r
            sequence.append(r)
        if right:
            total_seek += abs(current -right[-1])
            current = right[-1]
        for r in reversed(right[:-1]):
            total_seek += abs(current - r)
            current = r
            sequence.append(r)

    
    elif direction == "right":
        for r in right:
            total_seek += abs(current - r)
            current = r
            sequence.append(r)
        if left:
            total_seek += abs(current-left[0])
            current = left[0]
        for r in left[1:]:
            total_seek += abs(current - r)
            current = r
            sequence.append(r)

    
    
    return sequence, total_seek

sequence, total_seek = scan(requests, head, direction)

print("total seek time:", total_seek)