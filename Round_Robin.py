n = int(input("Enter number of processes: "))
pid = []
at = []
bt = []

for i in range(n):
    pid.append(f'P{i+1}')
    at.append(int(input(f"Enter Arrival Time for P{i+1}: ")))
    bt.append(int(input(f"Enter Burst Time for P{i+1}: ")))

q = int(input("Enter Time Quantum: "))

rt = bt[:]  
ct = [0]*n
t = 0
done = 0
rq = []

while done < n:
    for i in range(n):
        if at[i] <= t and rt[i] > 0 and i not in rq:
            rq.append(i)

    if rq:
        i = rq.pop(0)
        run = min(q, rt[i])
        t += run
        rt[i] -= run

        for j in range(n):
            if at[j] > t - run and at[j] <= t and rt[j] > 0 and j not in rq:
                rq.append(j)

        if rt[i] == 0:
            ct[i] = t
            done += 1
        else:
            rq.append(i)
    else:
        t += 1 

tat = [ct[i] - at[i] for i in range(n)]
wt = [tat[i] - bt[i] for i in range(n)]

print("\nPID\tAT\tBT\tCT\tTAT\tWT")
for i in range(n):
    print(f"{pid[i]}\t{at[i]}\t{bt[i]}\t{ct[i]}\t{tat[i]}\t{wt[i]}")

print(f"\nAverage TAT = {sum(tat)/n:.2f}")
print(f"Average WT  = {sum(wt)/n:.2f}")
