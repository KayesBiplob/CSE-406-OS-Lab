n = int(input("Number of processes: "))

p = []
for i in range(n):
    pid = input(f"Process ID for P{i+1}: ")
    pr = int(input(f"Priority for P{i+1}: "))         
    at = int(input(f"Arrival time for P{i+1}: "))     
    bt = int(input(f"Burst time for P{i+1}: "))       
    p.append([pid, pr, at, bt, 0, 0, 0]) 

time = 0
completed = 0
v = [False]*n

while completed < n:
    idx = -1
    min_pr = float('inf')

    for i in range(n):
        if not v[i] and p[i][2] <= time:         
            if p[i][1] < min_pr:                      
                min_pr = p[i][1]
                idx = i

    if idx == -1:
        time += 1
        continue

    time += p[idx][3]                                  
    p[idx][4] = time                                  
    p[idx][5] = p[idx][4] - p[idx][2]                 
    p[idx][6] = p[idx][5] - p[idx][3]                 
    v[idx] = True
    completed += 1

print("\nPID\tPR\tAT\tBT\tCT\tTAT\tWT")

for proc in p:
    print(f"{proc[0]}\t{proc[1]}\t{proc[2]}\t{proc[3]}\t{proc[4]}\t{proc[5]}\t{proc[6]}")
