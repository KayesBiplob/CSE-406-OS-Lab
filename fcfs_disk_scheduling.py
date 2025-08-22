requests = [176, 39, 114, 96, 26]
initial_head = 60

def fcfs(requests, head):
    total_head_movement = 0
    position = head
    movement = [head]

    for request in requests:
        if request == position:
            continue  

        distance = abs(request - position)
        total_head_movement += distance
        position = request
        movement.append(request)

    return movement, total_head_movement

sequence, total_movement = fcfs(requests, initial_head)

print("Head movement:", "->".join(map(str, sequence)))
print("Total number of head movements:", total_movement)
