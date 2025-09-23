#SJF CPU Scheduling
n = 4
pid = ["P1", "P2", "P3", "P4"]
at = [0, 1, 2, 3]
bt = [6, 8, 7, 3]

ct = [0]*n
tat = [0]*n
wt = [0]*n
done = [False]*n
t = 0
gantt = "|0|"
completed = 0

while completed<n:
    idx = -1
    min_bt = float('inf')
    for i in range(n):
        if at[i]<=t and not done[i] and bt[i] < min_bt:
            min_bt = bt[i]
            idx = i

    if idx == -1:
        t +=1
        gantt += f"IDLE|{t}|"
    
    else :
        t += bt[idx]
        ct[idx]=t
        done[idx] = True
        completed += 1
        gantt += f"{pid[idx]}|{t}|"

for i in range(n):
    tat[i] = ct[i]-at[i]
    wt[i] = tat[i]-bt[i]

print("\nProcess\tAT\tBT\tCT\tTAT\tWT")
for i in range(n):
    print(f"{pid[i]}\t{at[i]}\t{bt[i]}\t{ct[i]}\t{tat[i]}\t{wt[i]}")
print("\nGantt Chart: ",gantt)
print(f"Avg TAT= {sum(tat)/n:.2f}ms")
print(f"Avg WT= {sum(wt)/n:.2f}ms")