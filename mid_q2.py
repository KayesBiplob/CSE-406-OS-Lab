requests = [98,183,37,122,14,124,65,67]
head = 53

def sstf(requests, head):
    total_seek = 0
    current = head
    sequence = [head]
    pending = requests[:]

    while pending:
        nearest = min(pending, key= lambda a:abs(current-a))
        if nearest == current:
            pending.remove(nearest)
            continue
        total_seek += abs(current - nearest)
        current = nearest
        sequence.append(nearest)
        pending.remove(nearest)

    return sequence, total_seek

sequence, total_seek = sstf(requests, head)

print("Total Seek Time:", total_seek)
print("Sequence:","->".join(map(str,sequence)))
