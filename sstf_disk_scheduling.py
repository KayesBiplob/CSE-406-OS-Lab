requests = [26, 39, 49, 90, 114, 176]
head = 39

def sstf(requests, head):
    total_seek = 0
    current = head
    sequence = [head]  

    pending = requests[:]  

    while pending:
        nearest = min(pending, key=lambda a: abs(current - a))

        total_seek += abs(current - nearest)
        current = nearest
        sequence.append(nearest)
        pending.remove(nearest)

    return sequence, total_seek


sequence, total_seek = sstf(requests, head)

print("Sequence:", " -> ".join(map(str, sequence)))
print("Total seek time:", total_seek)
